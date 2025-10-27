# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .public_email_recipients import PublicEmailRecipients

__all__ = ["PublicEmailToDetails"]


class PublicEmailToDetails(BaseModel):
    contact_ids: Optional[PublicEmailRecipients] = FieldInfo(alias="contactIds", default=None)
    """Data structure representing lists of IDs that should be included and excluded."""

    contact_ils_lists: Optional[PublicEmailRecipients] = FieldInfo(alias="contactIlsLists", default=None)
    """Data structure representing lists of IDs that should be included and excluded."""

    contact_lists: Optional[PublicEmailRecipients] = FieldInfo(alias="contactLists", default=None)
    """Data structure representing lists of IDs that should be included and excluded."""

    limit_send_frequency: Optional[bool] = FieldInfo(alias="limitSendFrequency", default=None)

    suppress_graymail: Optional[bool] = FieldInfo(alias="suppressGraymail", default=None)
    """Whether to send to unengaged contacts (false) or not (true)."""
