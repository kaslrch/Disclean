from urllib.parse import ParseResult, urlencode, urlunparse as toString
def apply_query(uri: ParseResult, query: dict[str, list[str]]) -> ParseResult:
  return uri._replace(query=urlencode(query, doseq=True))

async def matches(
  url: str, uri: ParseResult,
  hostname: str, basedomain: str,
  pathname: str, query: dict[str, list[str]]
) -> str:
  if basedomain == "bing.com":  # chilling
    remove_keys = {"cvid", "form", "sk", "sp", "sc", "qs", "pq"}
    query = {k: v for k, v in query.items() if k not in remove_keys}
  return toString(apply_query(uri, query))
