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


class AdverseEventCountsTool(Tool):
    def _invoke(self, tool_parameters: dict[str, Any]) -> Generator[ToolInvokeMessage, None, None]:
        p = tool_parameters
        q = {
            "ingredient": (p.get("ingredient") or "").strip(),
            "species": p.get("species") or None,
            "source": p.get("source") or None,
            "year_from": _int(p.get("year_from")),
            "year_to": _int(p.get("year_to")),
            "limit": max(1, min(50, _int(p.get("limit")) or 25)),
        }
        yield from run(self, self.runtime.credentials.get("factdock_api_key"), lambda k: get(k, "/v1/adverse-events", q))
