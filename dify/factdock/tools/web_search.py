from collections.abc import Generator
from typing import Any

from dify_plugin import Tool
from dify_plugin.entities.tool import ToolInvokeMessage

from tools.factdock_api import call_engine, run, split_list


class WebSearchTool(Tool):
    def _invoke(self, tool_parameters: dict[str, Any]) -> Generator[ToolInvokeMessage, None, None]:
        p = tool_parameters
        args = {
            "query": p.get("query"),
            "zone": p.get("zone"),
            "intent": p.get("intent") or "local_voice",
            "time_range": p.get("time_range") or "any",
            "keywords": split_list(p.get("keywords"))[:8],
            "exclude_terms": split_list(p.get("exclude_terms"))[:10],
            "lang": p.get("lang") or "en",
        }
        yield from run(self, self.runtime.credentials.get("factdock_api_key"), lambda k: call_engine(k, "web_search", args))
