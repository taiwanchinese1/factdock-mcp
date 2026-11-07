from collections.abc import Generator
from typing import Any

from dify_plugin import Tool
from dify_plugin.entities.tool import ToolInvokeMessage

from tools.factdock_api import FactdockError, call_engine, get, run


class InsightsSearchTool(Tool):
    """Platform keys read Insights through the insights_feed engine; Insights API keys use /v1/insights/search."""

    def _invoke(self, tool_parameters: dict[str, Any]) -> Generator[ToolInvokeMessage, None, None]:
        p = tool_parameters
        country = (p.get("country") or "").strip().upper() or None
        category = (p.get("category") or "").strip().lower() or None
        lang = p.get("lang") or "en"
        limit = max(1, min(20, int(p.get("limit") or 10)))

        def go(k: str) -> dict[str, Any]:
            try:
                return call_engine(k, "insights_feed", {
                    "track": p.get("track") or "official",
                    "category": category,
                    "country": country,
                    "limit": limit,
                    "lang": lang,
                })
            except FactdockError as e:
                if e.status != 403:
                    raise
            # Insights API key: keyword search over the archive.
            return get(k, "/v1/insights/search", {
                "q": p.get("query") or "", "country": country, "category": category, "lang": lang, "limit": limit,
            })

        yield from run(self, self.runtime.credentials.get("factdock_api_key"), go)
