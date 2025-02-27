from urllib.parse import ParseResult
import aiohttp

async def fetch(url: str) -> str:
  async with aiohttp.ClientSession() as session:
    session.headers["User-Agent"] = "Twitterbot/1.0"
    async with session.get(url) as res:
      return await res.text()

async def matches(
  url: str, uri: ParseResult,
  hostname: str, basedomain: str,
  pathname: str, query: dict[str, list[str]]
) -> str:
  if hostname == "link.bgzt.in":
    text = await fetch(url)
    try:
      product_id = int(text.split("https://media.bunjang.co.kr/product/")[1].split("_")[0])
      return f"https://m.bunjang.co.kr{product_id}?redirect_global=false"
    except (IndexError, ValueError):
      return url

  if hostname == "m.bunjang.co.kr" and pathname.startswith("/products"):
    return f"https://m.bunjang.co.kr{pathname}?redirect_global=false"

  if hostname == "globalbunjang.com":
    return f"https://m.bunjang.co.kr{pathname.replace('/product/', '/products').replace('/search', '/search/products')}"

  return url
