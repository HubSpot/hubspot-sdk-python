# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ....._utils import PropertyInfo

__all__ = ["SettingUpdateParams"]


class SettingUpdateParams(TypedDict, total=False):
    height: int
    """The target height of the iframe that will contain your phone/calling UI."""

    is_ready: Annotated[bool, PropertyInfo(alias="isReady")]
    """When true, this indicates that your calling app is ready for production.

    Users will be able to select your calling app as their provider and can then
    click to dial within HubSpot.
    """

    name: str
    """The name of your calling service to display to users."""

    supports_custom_objects: Annotated[bool, PropertyInfo(alias="supportsCustomObjects")]
    """When true, users will be able to click to dial from custom objects."""

    supports_inbound_calling: Annotated[bool, PropertyInfo(alias="supportsInboundCalling")]
    """
    When true, this indicates that your calling app supports inbound calling within
    HubSpot.
    """

    url: str
    """The URL to your phone/calling UI, built with the [Calling SDK](#)."""

    uses_calling_window: Annotated[bool, PropertyInfo(alias="usesCallingWindow")]
    """
    When false, this indicates that your calling app does not require the use of the
    separate calling window to hold the call connection.
    """

    uses_remote: Annotated[bool, PropertyInfo(alias="usesRemote")]
    """
    When false, this indicates that your calling app does not use the anchored
    calling remote within the HubSpot app.
    """

    width: int
    """The target width of the iframe that will contain your phone/calling UI."""
