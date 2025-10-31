# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ....._utils import PropertyInfo

__all__ = ["SettingCreateParams"]


class SettingCreateParams(TypedDict, total=False):
    name: Required[str]

    url: Required[str]

    height: int

    is_ready: Annotated[bool, PropertyInfo(alias="isReady")]

    supports_custom_objects: Annotated[bool, PropertyInfo(alias="supportsCustomObjects")]

    supports_inbound_calling: Annotated[bool, PropertyInfo(alias="supportsInboundCalling")]

    uses_calling_window: Annotated[bool, PropertyInfo(alias="usesCallingWindow")]

    uses_remote: Annotated[bool, PropertyInfo(alias="usesRemote")]

    width: int
