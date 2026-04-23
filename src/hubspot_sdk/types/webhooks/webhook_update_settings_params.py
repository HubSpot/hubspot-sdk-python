# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo
from .throttling_settings_param import ThrottlingSettingsParam

__all__ = ["WebhookUpdateSettingsParams"]


class WebhookUpdateSettingsParams(TypedDict, total=False):
    target_url: Required[Annotated[str, PropertyInfo(alias="targetUrl")]]
    """The URL to which webhook events will be sent. It is a string."""

    throttling: Required[ThrottlingSettingsParam]
