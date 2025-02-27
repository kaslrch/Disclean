from discord import Message, TextChannel, Member # , Webhook, File
from urllib.parse import parse_qs, urlparse
from types import ModuleType
import importlib.util
import discord
import os, re

class MyClient(discord.Client):
  async def on_ready(self):
    print(f"Logged on as {self.user}!")
    self.rules = self.load_rules()

  async def on_message(self, message: Message):
    if message.author.bot:  return

    cleaned_content = await self.clean_url(message.content)
    if cleaned_content == message.content:  return

    if not hasattr(message.channel, "webhooks"):
      return await message.channel.send(cleaned_content)

    assert isinstance(message.channel, TextChannel)
    webhooks = await message.channel.webhooks()

    webhook = next((wh for wh in webhooks if wh.token), None)
    if webhook is None and len(webhooks) < 15:
      webhook = await message.channel.create_webhook(name="ClearURL")

    if webhook is None:
      return await message.channel.send(cleaned_content)

    if (
      not message.attachments
      and isinstance(message.author, Member)
      and message.channel.permissions_for(message.author).manage_messages
    ):  await message.delete()

    kwargs = {}
    if message.poll:
      kwargs["poll"] = message.poll

    # if message.attachments:
    #   kwargs["files"] = [
    #     File(fp=attachment.url, filename=attachment.filename)
    #     for attachment in message.attachments
    #   ]

    await webhook.send(cleaned_content,
      username=message.author.display_name,
      avatar_url=message.author.display_avatar.url,
      silent=True, **kwargs,
    )

  async def clean_url(self, text: str) -> str:
    async def replacer(match: re.Match) -> str:
      url = match.group(0)
      try:
        uri = urlparse(url)
        if not uri.hostname:  return url

        basedomain = ".".join(uri.hostname.split(".")[-2:])
        query = parse_qs(uri.query)

        for rule in self.rules:
          url = await rule.matches(
            url=url, uri=uri, hostname=uri.hostname,
            basedomain=basedomain, pathname=uri.path, query=query
          )
        return url
      except Exception:
        return url

    return await sub(r"https?:\/\/[^\s<]+[^<.,:;>)\]\s]", replacer, text)

  def load_rules(self) -> list[ModuleType]:
    rules = []

    for filename in sorted(
      [os.path.join("rules", f) for f in os.listdir("rules") if f.endswith(".py")],
      key=lambda x: (x != "zzz.py", x)  # zzz at last
    ):
      module_name = os.path.basename(filename)[:-3]
      spec = importlib.util.spec_from_file_location(module_name, filename)

      if not spec or not spec.loader:
        print(f"Failed to load module: {filename}")
        continue

      module = importlib.util.module_from_spec(spec)
      spec.loader.exec_module(module)

      if hasattr(module, "matches"):
        rules.append(module)

    return rules

async def sub(pattern: str, repl_async, text: str) -> str:
  result, last_end = "", 0
  for match in re.finditer(pattern, text):
    result += text[last_end: match.start()]
    result += await repl_async(match)
    last_end = match.end()
  return result + text[last_end:]

intents = discord.Intents.default()
intents.guilds = intents.moderation = intents.messages = True
intents.guild_messages = intents.webhooks = intents.message_content  = True

if __name__ == "__main__":
  token = os.getenv("DISCORD_TOKEN")
  if not token:
    print("Error: DISCORD_TOKEN environment variable is missing.")
    exit(1)
  client = MyClient(intents=intents)
  client.run(token)
