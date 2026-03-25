# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["PublicCampaignInfluencedFilterParam"]


class PublicCampaignInfluencedFilterParam(TypedDict, total=False):
    campaign_id: Required[Annotated[str, PropertyInfo(alias="campaignId")]]
    """The ID of the campaign that influences the filter."""

    filter_type: Required[Annotated[Literal["CAMPAIGN_INFLUENCED"], PropertyInfo(alias="filterType")]]
    """Indicates the type of filter (CAMPAIGN_INFLUENCED)."""
