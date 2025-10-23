# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["APISignatureWebhookAuthSettingsParam"]


class APISignatureWebhookAuthSettingsParam(TypedDict, total=False):
    app_id: Required[Annotated[int, PropertyInfo(alias="appId")]]
    """The appId that this signature will be generated for."""

    type: Required[Literal["SIGNATURE"]]
    """The type of webhook auth settings this is, can be: "AUTH_KEY" or "SIGNATURE" """
