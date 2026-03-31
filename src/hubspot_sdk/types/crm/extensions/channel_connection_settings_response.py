# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["ChannelConnectionSettingsResponse"]


class ChannelConnectionSettingsResponse(BaseModel):
    created_at: datetime = FieldInfo(alias="createdAt")
    """The date and time when the channel connection settings were created."""

    is_ready: bool = FieldInfo(alias="isReady")
    """Indicates whether the channel connection settings are ready for use."""

    updated_at: datetime = FieldInfo(alias="updatedAt")
    """The date and time when the channel connection settings were last updated."""

    url: str
    """The URL associated with the channel connection settings."""
