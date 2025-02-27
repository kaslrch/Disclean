from urllib.parse import ParseResult, urlencode, urlunparse as toString
def apply_query(uri: ParseResult, query: dict[str, list[str]]) -> ParseResult:
  return uri._replace(query=urlencode(query, doseq=True))

async def matches(
  url: str, uri: ParseResult,
  hostname: str, basedomain: str,
  pathname: str, query: dict[str, list[str]]
) -> str:
  if basedomain.endswith("bilibili.com"):
    query.pop("callback", None)
  return toString(apply_query(uri, query))
