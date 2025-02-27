from urllib.parse import ParseResult

async def matches(
  url: str, uri: ParseResult,
  hostname: str, basedomain: str,
  pathname: str, query: dict[str, list[str]]
) -> str:
  if basedomain in {"aliexpress.ru", "aliexpress.com"} and pathname.endswith(".html"):
    if pathname.startswith(("/item/", "/w/wholesale-")):
      return f"https://aliexpress.com{pathname}"
  return url
