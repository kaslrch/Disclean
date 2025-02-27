from urllib.parse import ParseResult, urlencode, urlunparse as toString
def applyQuery(uri: ParseResult, query: dict[str, list[str]]) -> ParseResult:
  return uri._replace(query=urlencode(query, doseq=True))

async def matches(
  url: str, uri: ParseResult,
  hostname: str, basedomain: str,
  pathname: str, query: dict[str, list[str]],
) -> str:
  try:
    if basedomain == "instagram.com" and query.get('igsh') != None:
      query.pop('igsh')
      return toString(applyQuery(uri, query))
  except:
    return url
  return url
