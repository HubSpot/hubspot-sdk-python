# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["CustomChannelCreateParams"]


class CustomChannelCreateParams(TypedDict, total=False):
    capabilities: Required[Dict[str, object]]

    name: Required[str]

    channel_account_connection_redirect_url: Annotated[str, PropertyInfo(alias="channelAccountConnectionRedirectUrl")]

    channel_description: Annotated[str, PropertyInfo(alias="channelDescription")]

    channel_logo_url: Annotated[str, PropertyInfo(alias="channelLogoUrl")]

    webhook_url: Annotated[str, PropertyInfo(alias="webhookUrl")]
