# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["ChannelConnectionSettingsResponse"]


class ChannelConnectionSettingsResponse(BaseModel):
    created_at: datetime = FieldInfo(alias="createdAt")

    is_ready: bool = FieldInfo(alias="isReady")

    updated_at: datetime = FieldInfo(alias="updatedAt")

    url: str
