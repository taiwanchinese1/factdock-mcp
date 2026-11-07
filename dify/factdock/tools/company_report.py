from collections.abc import Generator
from typing import Any

from dify_plugin import Tool
from dify_plugin.entities.tool import ToolInvokeMessage

from tools.factdock_api import call_engine, run


class CompanyReportTool(Tool):
    def _invoke(self, tool_parameters: dict[str, Any]) -> Generator[ToolInvokeMessage, None, None]:
        p = tool_parameters
        args = {
            "name": p.get("name"),
            "country": p.get("country"),
            "country_code": (p.get("country_code") or "").strip().upper(),
            "url": p.get("url"),
            "location": p.get("location"),
            "scope": p.get("scope") or "domestic",
            "include_governance": bool(p.get("include_governance")),
            "lang": p.get("lang") or "en",
        }
        yield from run(self, self.runtime.credentials.get("factdock_api_key"), lambda k: call_engine(k, "company_report", args))
