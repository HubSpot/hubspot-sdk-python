# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ....._utils import PropertyInfo

__all__ = ["SettingUpdateParams"]


class SettingUpdateParams(TypedDict, total=False):
    height: int

    is_ready: Annotated[bool, PropertyInfo(alias="isReady")]

    name: str

    supports_custom_objects: Annotated[bool, PropertyInfo(alias="supportsCustomObjects")]

    supports_inbound_calling: Annotated[bool, PropertyInfo(alias="supportsInboundCalling")]

    url: str

    uses_calling_window: Annotated[bool, PropertyInfo(alias="usesCallingWindow")]

    uses_remote: Annotated[bool, PropertyInfo(alias="usesRemote")]

    width: int
