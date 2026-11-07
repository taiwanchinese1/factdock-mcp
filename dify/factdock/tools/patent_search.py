from collections.abc import Generator
from typing import Any

from dify_plugin import Tool
from dify_plugin.entities.tool import ToolInvokeMessage

from tools.factdock_api import call_engine, run, split_list


class PatentSearchTool(Tool):
    def _invoke(self, tool_parameters: dict[str, Any]) -> Generator[ToolInvokeMessage, None, None]:
        p = tool_parameters
        offices = split_list(p.get("offices"), upper=True)
        if (p.get("offices") or "").strip().lower() == "major5":
            offices = ["US", "JP", "CN", "KR", "EP"]
        args = {
            "query": p.get("query"),
            "countries": offices,
            "period": p.get("period") or "wide",
            "cpc": p.get("cpc"),
            "lang": p.get("lang") or "en",
        }
        yield from run(self, self.runtime.credentials.get("factdock_api_key"), lambda k: call_engine(k, "patent_search", args))
