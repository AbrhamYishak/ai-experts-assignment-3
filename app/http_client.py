from __future__ import annotations

from typing import Any, Dict, Optional, Union

import requests
from datetime import datetime, timezone
from .tokens import OAuth2Token


class Client:
    def __init__(self) -> None:
        self.oauth2_token: Union[OAuth2Token, Dict[str, Any], None] = None
        self.session = requests.Session()

    def refresh_oauth2(self) -> None:
        self.oauth2_token = OAuth2Token(access_token="fresh-token", expires_at=10**10)

    def request(
        self,
        method: str,
        path: str,
        *,
        api: bool = False,
        headers: Optional[Dict[str, str]] = None,
    ) -> Dict[str, Any]:
        if headers is None:
            headers = {}

        if api:
            if not self.oauth2_token or (
                isinstance(self.oauth2_token, OAuth2Token) and (not self.oauth2_token.access_token or self.oauth2_token.expired)) or (
                isinstance(self.oauth2_token, dict) and (not self.oauth2_token.get("access_token") or int(datetime.now(tz=timezone.utc).timestamp()) >= self.oauth2_token.get("expires_at"))):
                self.refresh_oauth2()
            if isinstance(self.oauth2_token, OAuth2Token):
                headers["Authorization"] = self.oauth2_token.as_header()
            if isinstance(self.oauth2_token, dict):
                if self.oauth2_token.get("access_token"):
                    headers["Authorization"] = f"Bearer {self.oauth2_token.get('access_token')}"


        req = requests.Request(method=method, url=f"https://example.com{path}", headers=headers)
        prepared = self.session.prepare_request(req)

        return {
            "method": method,
            "path": path,
            "headers": dict(prepared.headers),
        }