from collections.abc import Generator
from typing import Any

from dify_plugin import Tool
from dify_plugin.entities.tool import ToolInvokeMessage

from tools.factdock_api import FactdockError, call_engine, run, split_list


class FinanceSearchTool(Tool):
    def _invoke(self, tool_parameters: dict[str, Any]) -> Generator[ToolInvokeMessage, None, None]:
        p = tool_parameters
        codes = split_list(p.get("country_codes"), upper=True)[:3]
        names = split_list(p.get("country_names"))[:3]
        categories = split_list(p.get("categories"))[:12] or ["gdp", "inflation", "policy_rate", "fx"]

        def go(k: str) -> dict[str, Any]:
            if not codes or len(codes) != len(names):
                raise FactdockError("Give the same number of country codes and English country names (up to 3), e.g. 'JP, DE' and 'Japan, Germany'.")
            countries = [{"code": c, "name": n} for c, n in zip(codes, names)]
            return call_engine(k, "finance_search", {"countries": countries, "categories": categories, "lang": p.get("lang") or "en"})

        yield from run(self, self.runtime.credentials.get("factdock_api_key"), go)
