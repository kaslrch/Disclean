from urllib.parse import ParseResult, urlencode, urlunparse as toString
def apply_query(uri: ParseResult, query: dict[str, list[str]]) -> ParseResult:
  return uri._replace(query=urlencode(query, doseq=True))

remove_prefixes = {"pk_", "ga_", "itm_", "utm_", "gs_", "gws_", "fb_"}
remove_keys = [
  "Campaign", "__hssc", "__hstc", "_hsenc", "_hsmi", "_openstat",
  "action_object_map", "action_ref_map", "action_type_map", "aff_platform",
  "aff_trace_key", "assetId", "assetType", "btsid", "c_id", "campaignId",
  "campaign_id", "cmpid", "elqTrack", "elqTrackId", "fbclid", "gclid",
  "gclsrc", "hmb_campaign", "hmb_medium", "hmb_source", "hrc", "hsCtaTracking", "igsh",
  "igshid", "mbid", "mc_cid", "mc_eid", "mkt_tok", "nr_email_referer", "pq",
  "qs", "recipientId", "redircnt", "refsrc", "s_cid", "sc", "sc_campaign", "sc_channel",
  "sc_cid", "sc_content", "sc_country", "sc_geo", "sc_medium", "sc_outcome", "scm",
  "share_id", "si", "siteId", "sk", "sp", "spJobID", "spMailingID", "spReportId",
  "spUserID", "spm", "trk", "trkCampaign", "tt_content", "tt_medium", "vero_conv",
  "vero_id", "ws_ab_test", "wt_zmc", "yclid",
]

async def matches(
  url: str, uri: ParseResult,
  hostname: str, basedomain: str,
  pathname: str, query: dict[str, list[str]]
) -> str:
  try:
    query = {k: v for k, v in query.items() if k not in remove_keys}
    query = {k: v for k, v in query.items() if not any(k.startswith(p) for p in remove_prefixes)}
    return toString(apply_query(uri, query))
  except:
    return url
