# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["APIAuthKeyWebhookAuthSettings"]


class APIAuthKeyWebhookAuthSettings(BaseModel):
    location: Literal["HEADER", "QUERY_PARAM"]
    """Where in the request this auth key should be located: "HEADER" or "QUERY_PARAM" """

    name: str
    """The name to use for this auth key."""

    secret_name: str = FieldInfo(alias="secretName")
    """The secret to pass through in this auth key."""

    type: Literal["AUTH_KEY"]
    """The type of webhook auth settings this is, can be: "AUTH_KEY" or "SIGNATURE" """
