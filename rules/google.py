from urllib.parse import ParseResult, urlencode, urlunparse as toString
def apply_query(uri: ParseResult, query: dict[str, list[str]]) -> ParseResult:
  return uri._replace(query=urlencode(query, doseq=True))

async def matches(
  url: str, uri: ParseResult,
  hostname: str, basedomain: str,
  pathname: str, query: dict[str, list[str]]
) -> str:
  if hostname in {"google.com", "www.google.com"}:
    keep_keys = {"udm", "hl", "q"}
    filtered_query = {k: v for k, v in query.items() if k in keep_keys}
    return toString(apply_query(uri, filtered_query))

  return url
