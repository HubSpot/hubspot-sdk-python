# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from ..shared.forward_paging import ForwardPaging

__all__ = ["CustomChannelListResponse", "Result"]


class Result(BaseModel):
    id: str

    capabilities: Dict[str, object]

    created_at: datetime = FieldInfo(alias="createdAt")

    name: str

    channel_account_connection_redirect_url: Optional[str] = FieldInfo(
        alias="channelAccountConnectionRedirectUrl", default=None
    )

    channel_description: Optional[str] = FieldInfo(alias="channelDescription", default=None)

    channel_logo_url: Optional[str] = FieldInfo(alias="channelLogoUrl", default=None)

    webhook_url: Optional[str] = FieldInfo(alias="webhookUrl", default=None)


class CustomChannelListResponse(BaseModel):
    results: List[Result]

    total: int

    paging: Optional[ForwardPaging] = None
