from collections.abc import Generator
from typing import Any

from dify_plugin import Tool
from dify_plugin.entities.tool import ToolInvokeMessage

from tools.factdock_api import call_engine, run, split_list


class AcademicSearchTool(Tool):
    def _invoke(self, tool_parameters: dict[str, Any]) -> Generator[ToolInvokeMessage, None, None]:
        p = tool_parameters
        args = {
            "query": p.get("query"),
            "purpose": p.get("purpose"),
            "max_results": int(p.get("max_results") or 60),
            "exclude_terms": split_list(p.get("exclude_terms"))[:10],
            "lang": p.get("lang") or "en",
        }
        yield from run(self, self.runtime.credentials.get("factdock_api_key"), lambda k: call_engine(k, "academic_search", args))
