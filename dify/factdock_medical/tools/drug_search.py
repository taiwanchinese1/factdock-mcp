from collections.abc import Generator
from typing import Any

from dify_plugin import Tool
from dify_plugin.entities.tool import ToolInvokeMessage

from tools.factdock_api import get, run


def _int(v: Any) -> int | None:
    try:
        return int(v) if v not in (None, "") else None
    except (TypeError, ValueError):
        return None


class DrugSearchTool(Tool):
    def _invoke(self, tool_parameters: dict[str, Any]) -> Generator[ToolInvokeMessage, None, None]:
        p = tool_parameters
        q = {
            "q": (p.get("query") or "").strip(),
            "target": p.get("target") or None,
            "country": (p.get("country") or "").strip().upper() or None,
            "species": p.get("species") or None,
            "limit": max(1, min(20, _int(p.get("limit")) or 10)),
        }
        yield from run(self, self.runtime.credentials.get("factdock_api_key"), lambda k: get(k, "/v1/drugs/search", q))
