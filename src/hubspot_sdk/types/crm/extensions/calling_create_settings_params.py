# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["CallingCreateSettingsParams"]


class CallingCreateSettingsParams(TypedDict, total=False):
    height: Required[int]
    """Specifies the height of the calling extension interface."""

    is_ready: Required[Annotated[bool, PropertyInfo(alias="isReady")]]
    """Indicates if the calling extension is ready for use."""

    name: Required[str]
    """The name of the calling extension."""

    supports_custom_objects: Required[Annotated[bool, PropertyInfo(alias="supportsCustomObjects")]]
    """Indicates if the calling extension supports custom objects."""

    supports_inbound_calling: Required[Annotated[bool, PropertyInfo(alias="supportsInboundCalling")]]
    """Indicates if the calling extension supports inbound calling."""

    url: Required[str]
    """The URL associated with the calling extension."""

    uses_calling_window: Required[Annotated[bool, PropertyInfo(alias="usesCallingWindow")]]
    """Indicates if the calling extension uses a separate calling window."""

    uses_remote: Required[Annotated[bool, PropertyInfo(alias="usesRemote")]]
    """Indicates if the calling extension uses remote services."""

    width: Required[int]
    """Specifies the width of the calling extension interface."""
