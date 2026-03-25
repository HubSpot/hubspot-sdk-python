# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["OAuthCreateTokenParams"]


class OAuthCreateTokenParams(TypedDict, total=False):
    client_id: str

    client_secret: str

    code: str

    code_verifier: str

    grant_type: Literal["authorization_code", "refresh_token"]

    redirect_uri: str

    refresh_token: str

    scope: str
