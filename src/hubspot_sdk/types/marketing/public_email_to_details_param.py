# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo
from .public_email_recipients_param import PublicEmailRecipientsParam

__all__ = ["PublicEmailToDetailsParam"]


class PublicEmailToDetailsParam(TypedDict, total=False):
    contact_ids: Annotated[PublicEmailRecipientsParam, PropertyInfo(alias="contactIds")]
    """Data structure representing lists of IDs that should be included and excluded."""

    contact_ils_lists: Annotated[PublicEmailRecipientsParam, PropertyInfo(alias="contactIlsLists")]
    """Data structure representing lists of IDs that should be included and excluded."""

    contact_lists: Annotated[PublicEmailRecipientsParam, PropertyInfo(alias="contactLists")]
    """Data structure representing lists of IDs that should be included and excluded."""

    limit_send_frequency: Annotated[bool, PropertyInfo(alias="limitSendFrequency")]

    suppress_graymail: Annotated[bool, PropertyInfo(alias="suppressGraymail")]
    """Whether to send to unengaged contacts (false) or not (true)."""
