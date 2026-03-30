# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["SmtpTokenListParams"]


class SmtpTokenListParams(TypedDict, total=False):
    after: str
    """
    The paging cursor token of the last successfully read resource will be returned
    as the `paging.next.after` JSON property of a paged response containing more
    results.
    """

    campaign_name: Annotated[str, PropertyInfo(alias="campaignName")]

    email_campaign_id: Annotated[str, PropertyInfo(alias="emailCampaignId")]

    limit: int
    """The maximum number of results to display per page."""
