from collections.abc import Generator
from typing import Any

from dify_plugin import Tool
from dify_plugin.entities.tool import ToolInvokeMessage

from tools.factdock_api import get, run


def _params(p: dict[str, Any]) -> dict[str, Any]:
    return {
        "country": (p.get("country") or "").strip().upper() or None,
        "category": (p.get("category") or "").strip().lower() or None,
        "since": (p.get("since") or "").strip() or None,
        "lang": (p.get("lang") or "").strip() or None,
        "limit": max(1, min(20, int(p.get("limit") or 10))),
    }


class InsightsLatestTool(Tool):
    def _invoke(self, tool_parameters: dict[str, Any]) -> Generator[ToolInvokeMessage, None, None]:
        q = _params(tool_parameters)
        yield from run(self, self.runtime.credentials.get("factdock_api_key"), lambda k: get(k, "/v1/insights", q))
