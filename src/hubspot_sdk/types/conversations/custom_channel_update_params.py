# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["CustomChannelUpdateParams"]


class CustomChannelUpdateParams(TypedDict, total=False):
    capabilities: Required[Dict[str, object]]

    channel_account_connection_redirect_url: Required[
        Annotated[object, PropertyInfo(alias="channelAccountConnectionRedirectUrl")]
    ]

    channel_description: Required[Annotated[object, PropertyInfo(alias="channelDescription")]]

    channel_logo_url: Required[Annotated[object, PropertyInfo(alias="channelLogoUrl")]]

    name: Required[object]

    webhook_url: Required[Annotated[object, PropertyInfo(alias="webhookUrl")]]
