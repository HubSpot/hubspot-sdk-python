# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["SettingsResponse"]


class SettingsResponse(BaseModel):
    created_at: datetime = FieldInfo(alias="createdAt")
    """The date and time when the calling extension settings were created."""

    height: int
    """The height of the calling extension interface."""

    is_ready: bool = FieldInfo(alias="isReady")
    """Specifies whether the calling extension settings are ready for use."""

    name: str
    """The name of the calling extension."""

    supports_custom_objects: bool = FieldInfo(alias="supportsCustomObjects")
    """Indicates if the calling extension supports custom objects."""

    supports_inbound_calling: bool = FieldInfo(alias="supportsInboundCalling")
    """Indicates if the calling extension supports inbound calling."""

    updated_at: datetime = FieldInfo(alias="updatedAt")
    """The date and time when the calling extension settings were last updated."""

    url: str
    """The URL associated with the calling extension."""

    uses_calling_window: bool = FieldInfo(alias="usesCallingWindow")
    """Specifies if the calling extension uses a dedicated calling window."""

    uses_remote: bool = FieldInfo(alias="usesRemote")
    """Indicates if the calling extension uses a remote service."""

    width: int
    """The width of the calling extension interface."""
