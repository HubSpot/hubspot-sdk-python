# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .throttling_settings import ThrottlingSettings

__all__ = ["SettingsResponse"]


class SettingsResponse(BaseModel):
    created_at: datetime = FieldInfo(alias="createdAt")
    """The date and time when the webhook settings were created, in ISO 8601 format."""

    target_url: str = FieldInfo(alias="targetUrl")
    """The URL to which the webhook events will be sent. It is a string."""

    throttling: ThrottlingSettings

    updated_at: Optional[datetime] = FieldInfo(alias="updatedAt", default=None)
    """
    The date and time when the webhook settings were last updated, in ISO 8601
    format.
    """
