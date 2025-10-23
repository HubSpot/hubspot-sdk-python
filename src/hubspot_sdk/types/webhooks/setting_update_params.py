# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo
from .throttling_settings_param import ThrottlingSettingsParam

__all__ = ["SettingUpdateParams"]


class SettingUpdateParams(TypedDict, total=False):
    target_url: Required[Annotated[str, PropertyInfo(alias="targetUrl")]]
    """
    A publicly available URL for HubSpot to call where event payloads will be
    delivered.
    """

    throttling: Required[ThrottlingSettingsParam]
    """Configuration details for webhook throttling."""
