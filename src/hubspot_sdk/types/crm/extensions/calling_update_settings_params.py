# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["CallingUpdateSettingsParams"]


class CallingUpdateSettingsParams(TypedDict, total=False):
    height: int
    """The height setting for the calling extension interface."""

    is_ready: Annotated[bool, PropertyInfo(alias="isReady")]
    """Specifies whether the calling extension is ready for use."""

    name: str
    """The name of the calling extension."""

    supports_custom_objects: Annotated[bool, PropertyInfo(alias="supportsCustomObjects")]
    """Indicates if the calling extension supports custom objects."""

    supports_inbound_calling: Annotated[bool, PropertyInfo(alias="supportsInboundCalling")]
    """Indicates if the calling extension supports inbound calling."""

    url: str
    """The URL associated with the calling extension settings."""

    uses_calling_window: Annotated[bool, PropertyInfo(alias="usesCallingWindow")]
    """Indicates if the calling extension uses a calling window."""

    uses_remote: Annotated[bool, PropertyInfo(alias="usesRemote")]
    """Indicates if the calling extension uses a remote connection."""

    width: int
    """The width setting for the calling extension interface."""
