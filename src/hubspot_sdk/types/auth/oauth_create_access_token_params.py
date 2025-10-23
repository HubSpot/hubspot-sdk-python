# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["OAuthCreateAccessTokenParams"]


class OAuthCreateAccessTokenParams(TypedDict, total=False):
    client_id: str

    client_secret: str

    code: str

    grant_type: Literal["authorization_code", "refresh_token"]

    redirect_uri: str

    refresh_token: str
