# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["SmtpAPITokenView"]


class SmtpAPITokenView(BaseModel):
    """
    A SMTP API token provides both an ID and password that can be used to send email through the HubSpot SMTP API.
    """

    id: str
    """User name to log into the HubSpot SMTP server."""

    campaign_name: str = FieldInfo(alias="campaignName")
    """A name for the campaign tied to the token."""

    create_contact: bool = FieldInfo(alias="createContact")
    """Indicates whether a contact should be created for email recipients."""

    created_at: datetime = FieldInfo(alias="createdAt")
    """Timestamp generated when a token is created."""

    created_by: str = FieldInfo(alias="createdBy")
    """Email address of the user that sent the token creation request."""

    email_campaign_id: str = FieldInfo(alias="emailCampaignId")
    """Identifier assigned to the campaign provided in the token creation request."""

    password: Optional[str] = None
    """Password used to log into the HubSpot SMTP server."""
