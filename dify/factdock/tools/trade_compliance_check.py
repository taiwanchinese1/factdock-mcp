from collections.abc import Generator
from typing import Any

from dify_plugin import Tool
from dify_plugin.entities.tool import ToolInvokeMessage

from tools.factdock_api import call_engine, run


def _cc(v: Any) -> str | None:
    s = str(v or "").strip().upper()
    return s or None


class TradeComplianceCheckTool(Tool):
    def _invoke(self, tool_parameters: dict[str, Any]) -> Generator[ToolInvokeMessage, None, None]:
        p = tool_parameters
        args = {
            "mode": p.get("mode"),
            "product": p.get("product"),
            "hs_code": p.get("hs_code"),
            "origin_country": p.get("origin_country"),
            "origin_code": _cc(p.get("origin_code")),
            "dest_country": p.get("dest_country"),
            "dest_code": _cc(p.get("dest_code")),
            "company": p.get("company"),
            "company_url": p.get("company_url"),
            "company_country": p.get("company_country"),
            "company_code": _cc(p.get("company_code")),
            "lang": p.get("lang") or "en",
        }
        yield from run(self, self.runtime.credentials.get("factdock_api_key"), lambda k: call_engine(k, "trade_compliance_check", args))
