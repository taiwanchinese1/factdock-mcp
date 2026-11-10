"""Small client for the Factdock Business API (https://data.fact-dock.com).

Every call sends the API key as a Bearer header and uses the key holder's API credits.
Nothing is stored by this plugin.
"""

from __future__ import annotations

from collections.abc import Generator
from typing import Any

import requests

BASE_URL = "https://data.fact-dock.com"
USER_AGENT = "factdock-medical-dify-plugin/0.0.1"
TIMEOUT = (10, 90)


class FactdockError(Exception):
    def __init__(self, message: str, status: int | None = None) -> None:
        super().__init__(message)
        self.status = status


def _headers(api_key: str) -> dict[str, str]:
    return {"Authorization": f"Bearer {api_key}", "User-Agent": USER_AGENT, "Accept": "application/json"}


def _message(resp: requests.Response) -> str:
    try:
        body = resp.json()
    except ValueError:
        body = None
    detail = body.get("detail") if isinstance(body, dict) else None
    if isinstance(detail, dict):
        detail = detail.get("message")
    text = str(detail or "").strip()
    if resp.status_code == 401:
        return "The Factdock API key is not valid or has been revoked."
    if resp.status_code == 402:
        return text or "Not enough Factdock API credits."
    if resp.status_code == 403:
        return text or "This Factdock API key cannot use the medical database. Use a Medical DB key."
    if resp.status_code == 429:
        return text or "Too many requests or the daily credit cap was reached. Try again later."
    return text or f"Factdock returned HTTP {resp.status_code}."


def list_tools(api_key: str) -> list[dict[str, Any]]:
    resp = requests.get(f"{BASE_URL}/v1/engines", headers=_headers(api_key), timeout=(10, 30))
    if resp.status_code != 200:
        raise FactdockError(_message(resp))
    return resp.json().get("tools") or []


def get(api_key: str, path: str, params: dict[str, Any]) -> dict[str, Any]:
    q = {k: v for k, v in params.items() if v not in (None, "")}
    resp = requests.get(f"{BASE_URL}{path}", headers=_headers(api_key), params=q, timeout=TIMEOUT)
    if resp.status_code != 200:
        raise FactdockError(_message(resp), resp.status_code)
    return resp.json()


def split_list(value: Any, upper: bool = False) -> list[str]:
    """'JP, US' -> ['JP', 'US'] (Dify passes list inputs as text)."""
    items = [s.strip() for s in str(value or "").replace("\n", ",").split(",") if s.strip()]
    return [s.upper() for s in items] if upper else items


def run(tool_obj: Any, api_key: str | None, fn) -> Generator[Any, None, None]:
    """Shared wrapper: checks the key, runs `fn(api_key)`, and turns errors into a readable text message."""
    if not api_key:
        yield tool_obj.create_text_message("Factdock API key is missing. Add it in the plugin settings.")
        return
    try:
        out = fn(api_key)
    except FactdockError as e:
        yield tool_obj.create_text_message(f"Factdock: {e}")
        return
    except requests.Timeout:
        yield tool_obj.create_text_message(
            "Factdock did not answer in time. The request may still have been counted: check the credit history on the Factdock for Developers page before retrying."
        )
        return
    except requests.RequestException as e:
        yield tool_obj.create_text_message(f"Could not reach Factdock: {e}")
        return
    yield tool_obj.create_json_message(out)
