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


class DrugDetailTool(Tool):
    def _invoke(self, tool_parameters: dict[str, Any]) -> Generator[ToolInvokeMessage, None, None]:
        p = tool_parameters
        drug_id = _int(p.get("drug_id"))
        if not drug_id or drug_id < 1:
            yield self.create_text_message("Factdock: a drug id from Search approved drugs is required.")
            return
        yield from run(self, self.runtime.credentials.get("factdock_api_key"), lambda k: get(k, f"/v1/drugs/{drug_id}", {}))
