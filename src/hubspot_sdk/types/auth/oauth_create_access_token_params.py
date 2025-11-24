# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["OAuthCreateAccessTokenParams"]


class OAuthCreateAccessTokenParams(TypedDict, total=False):
    query_client_secret: Annotated[str, PropertyInfo(alias="client_secret")]

    query_refresh_token: Annotated[str, PropertyInfo(alias="refresh_token")]

    client_id: str

    body_client_secret: Annotated[str, PropertyInfo(alias="client_secret")]

    code: str

    code_verifier: str

    grant_type: Literal["authorization_code", "client_credentials", "refresh_token"]

    redirect_uri: str

    body_refresh_token: Annotated[str, PropertyInfo(alias="refresh_token")]

    scope: str
