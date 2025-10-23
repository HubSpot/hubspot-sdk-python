# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["APISignatureWebhookAuthSettings"]


class APISignatureWebhookAuthSettings(BaseModel):
    app_id: int = FieldInfo(alias="appId")
    """The appId that this signature will be generated for."""

    type: Literal["SIGNATURE"]
    """The type of webhook auth settings this is, can be: "AUTH_KEY" or "SIGNATURE" """
