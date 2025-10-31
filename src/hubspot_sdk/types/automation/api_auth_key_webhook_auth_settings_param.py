# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["APIAuthKeyWebhookAuthSettingsParam"]


class APIAuthKeyWebhookAuthSettingsParam(TypedDict, total=False):
    location: Required[Literal["HEADER", "QUERY_PARAM"]]

    name: Required[str]

    secret_name: Required[Annotated[str, PropertyInfo(alias="secretName")]]

    type: Required[Literal["AUTH_KEY"]]
