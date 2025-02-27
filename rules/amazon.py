from urllib.parse import ParseResult, urlencode, urlunparse as toString
def apply_query(uri: ParseResult, query: dict[str, list[str]]) -> ParseResult:
  return uri._replace(query=urlencode(query, doseq=True))

remove_keys = {
  "_encoding", "psc", "tag", "ref", "pf", "crid", "keywords",
  "sprefix", "sr", "ie", "node", "qid"
}
remove_prefixes = {"pf_rd_", "pd_rd_"}

async def matches(
  url: str, uri: ParseResult,
  hostname: str, basedomain: str,
  pathname: str, query: dict[str, list[str]]
) -> str:
  if basedomain.startswith("amazon."):
    query = {k: v for k, v in query.items() if k not in remove_keys and not any(k.startswith(p) for p in remove_prefixes)}

  return toString(apply_query(uri, query))
