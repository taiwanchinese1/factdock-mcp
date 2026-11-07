from collections.abc import Generator
from typing import Any

from dify_plugin import Tool
from dify_plugin.entities.tool import ToolInvokeMessage

from tools.factdock_api import call_engine, run, split_list


class GovInfraSearchTool(Tool):
    def _invoke(self, tool_parameters: dict[str, Any]) -> Generator[ToolInvokeMessage, None, None]:
        p = tool_parameters
        args = {
            "country": p.get("country"),
            "country_code": (p.get("country_code") or "").strip().upper(),
            "categories": split_list(p.get("sectors"))[:20],
            "city": p.get("city"),
            "lang": p.get("lang") or "en",
        }
        yield from run(self, self.runtime.credentials.get("factdock_api_key"), lambda k: call_engine(k, "gov_infra_search", args))
