from urllib.parse import ParseResult, urlencode, urlunparse as toString
def apply_query(uri: ParseResult, query: dict[str, list[str]]) -> ParseResult:
  return uri._replace(query=urlencode(query, doseq=True))

def remove_keys(query: dict[str, list[str]], *keys) -> dict[str, list[str]]:
  for key in keys:
    query.pop(key, None)
  return query

async def matches(
  url: str, uri: ParseResult,
  hostname: str, basedomain: str,
  pathname: str, query: dict[str, list[str]]
) -> str:
  if basedomain in {"youtube.com", "youtu.be"}:
    query = remove_keys(query, "si", "feature", "kw")
    # whitelist?: t,v,list, time_start etc
    # TODO: Option to strip ?list or 'music.' by User
  return toString(apply_query(uri, query))
