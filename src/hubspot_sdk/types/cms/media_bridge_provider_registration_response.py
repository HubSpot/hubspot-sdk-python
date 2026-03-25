# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["MediaBridgeProviderRegistrationResponse"]


class MediaBridgeProviderRegistrationResponse(BaseModel):
    app_id: int = FieldInfo(alias="appId")

    name: str
