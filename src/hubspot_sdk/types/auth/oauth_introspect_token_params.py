# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["OAuthIntrospectTokenParams"]


class OAuthIntrospectTokenParams(TypedDict, total=False):
    token: str

    client_id: str

    client_secret: str

    token_type_hint: str
