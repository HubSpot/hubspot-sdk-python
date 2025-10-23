# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["APIAuthKeyWebhookAuthSettingsParam"]


class APIAuthKeyWebhookAuthSettingsParam(TypedDict, total=False):
    location: Required[Literal["HEADER", "QUERY_PARAM"]]
    """Where in the request this auth key should be located: "HEADER" or "QUERY_PARAM" """

    name: Required[str]
    """The name to use for this auth key."""

    secret_name: Required[Annotated[str, PropertyInfo(alias="secretName")]]
    """The secret to pass through in this auth key."""

    type: Required[Literal["AUTH_KEY"]]
    """The type of webhook auth settings this is, can be: "AUTH_KEY" or "SIGNATURE" """
