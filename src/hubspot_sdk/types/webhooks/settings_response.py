# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .throttling_settings import ThrottlingSettings

__all__ = ["SettingsResponse"]


class SettingsResponse(BaseModel):
    """Webhook settings for an app."""

    created_at: datetime = FieldInfo(alias="createdAt")
    """When this subscription was created.

    Formatted as milliseconds from the [Unix epoch](#).
    """

    target_url: str = FieldInfo(alias="targetUrl")
    """
    A publicly available URL for HubSpot to call where event payloads will be
    delivered. See [link-so-some-doc](#) for details about the format of these event
    payloads.
    """

    throttling: ThrottlingSettings
    """Configuration details for webhook throttling."""

    updated_at: Optional[datetime] = FieldInfo(alias="updatedAt", default=None)
    """When this subscription was last updated.

    Formatted as milliseconds from the [Unix epoch](#).
    """
