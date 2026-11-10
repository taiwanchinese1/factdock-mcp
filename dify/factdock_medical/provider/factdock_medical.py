from typing import Any

from dify_plugin import ToolProvider
from dify_plugin.errors.tool import ToolProviderCredentialValidationError

from tools.factdock_api import FactdockError, list_tools


class FactdockMedicalProvider(ToolProvider):
    def _validate_credentials(self, credentials: dict[str, Any]) -> None:
        # Listing the tools is free, so checking the key never uses credits.
        api_key = (credentials.get("factdock_api_key") or "").strip()
        if not api_key:
            raise ToolProviderCredentialValidationError("Factdock API key is missing.")
        try:
            list_tools(api_key)
        except FactdockError as e:
            raise ToolProviderCredentialValidationError(str(e)) from e
        except Exception as e:  # network errors
            raise ToolProviderCredentialValidationError(f"Could not reach Factdock: {e}") from e
