# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ....._utils import PropertyInfo

__all__ = ["SettingCreateParams"]


class SettingCreateParams(TypedDict, total=False):
    height: Required[int]

    is_ready: Required[Annotated[bool, PropertyInfo(alias="isReady")]]

    name: Required[str]

    supports_custom_objects: Required[Annotated[bool, PropertyInfo(alias="supportsCustomObjects")]]

    supports_inbound_calling: Required[Annotated[bool, PropertyInfo(alias="supportsInboundCalling")]]

    url: Required[str]

    uses_calling_window: Required[Annotated[bool, PropertyInfo(alias="usesCallingWindow")]]

    uses_remote: Required[Annotated[bool, PropertyInfo(alias="usesRemote")]]

    width: Required[int]
