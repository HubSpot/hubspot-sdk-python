# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["PublicCampaignInfluencedFilter"]


class PublicCampaignInfluencedFilter(BaseModel):
    campaign_id: str = FieldInfo(alias="campaignId")

    filter_type: Literal["CAMPAIGN_INFLUENCED"] = FieldInfo(alias="filterType")
