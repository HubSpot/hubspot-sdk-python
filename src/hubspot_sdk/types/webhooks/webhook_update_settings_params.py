# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo
from .throttling_settings_param import ThrottlingSettingsParam

__all__ = ["WebhookUpdateSettingsParams"]


class WebhookUpdateSettingsParams(TypedDict, total=False):
    target_url: Required[Annotated[str, PropertyInfo(alias="targetUrl")]]
    """
    A publicly available URL for Hubspot to call where event payloads will be
    delivered. See [link-so-some-doc](#) for details about the format of these event
    payloads.
    """

    throttling: Required[ThrottlingSettingsParam]
