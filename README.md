# Disclean

## Installation
```sh
git clone https://github.com/kaslrch/Disclean.git
cd Disclean
python3 -m venv .venv
```
- Linux:
  ```sh
  chmod +x .venv/bin/activate && . .venv/bin/activate
  ```
- Windows:
  ```cmd
  .venv\Scripts\activate
  ```

Then, install dependencies:
```sh
pip install -r requirements.txt
```

## Usage
- Linux:
  ```sh
  . .venv/bin/activate && DISCORD_TOKEN=your_token python3 main.py
  ```
- Windows (cmd):
  ```cmd
  .venv\Scripts\activate && set DISCORD_TOKEN=your_token && python main.py
  ```
- Windows (PowerShell):
  ```pwsh
  .venv\Scripts\Activate; $env.DISCORD_TOKEN = 'your_token'; python main.py
  ```

## License
Disclean is licensed under the **[MIT](LICENSE)**.

This project uses third-party libraries:
- [**discord.py**](https://github.com/Rapptz/discord.py) ([MIT](https://github.com/Rapptz/discord.py/blob/master/LICENSE))
- [**aiohttp**](https://github.com/aio-libs/aiohttp) ([Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0))
- [NOTICE](NOTICE)

## Notice
- This bot replaces messages containing tracking parameters with cleaned URLs.
- If the user has ***Manage Messages*** permission and the message contains no attachments, the original message may be deleted.
- Webhooks are used for re-sending messages, meaning messages may not be editable or deletable by the original sender.
- **Issues and Pull Requests are always welcome!** (Especially for incorrectly cleaned or uncleaned URLs.)
