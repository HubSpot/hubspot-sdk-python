# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["SmtpTokenCreateParams"]


class SmtpTokenCreateParams(TypedDict, total=False):
    campaign_name: Required[Annotated[str, PropertyInfo(alias="campaignName")]]
    """A name for the campaign tied to the SMTP API token."""

    create_contact: Required[Annotated[bool, PropertyInfo(alias="createContact")]]
    """Indicates whether a contact should be created for email recipients."""
