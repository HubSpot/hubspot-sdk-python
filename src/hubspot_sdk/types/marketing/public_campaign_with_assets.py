# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List
from datetime import datetime

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .public_business_unit import PublicBusinessUnit
from .collection_response_public_campaign_asset import CollectionResponsePublicCampaignAsset

__all__ = ["PublicCampaignWithAssets"]


class PublicCampaignWithAssets(BaseModel):
    id: str
    """The unique identifier for the campaign."""

    assets: Dict[str, CollectionResponsePublicCampaignAsset]
    """
    A map of asset types to their corresponding collection of campaign assets,
    represented by CollectionResponsePublicCampaignAsset objects.
    """

    business_units: List[PublicBusinessUnit] = FieldInfo(alias="businessUnits")
    """
    An array of business units associated with the campaign, each represented by a
    PublicBusinessUnit object.
    """

    created_at: datetime = FieldInfo(alias="createdAt")
    """The date and time when the campaign was created, in ISO 8601 format."""

    properties: Dict[str, str]
    """A map of custom property names to their values for the campaign."""

    updated_at: datetime = FieldInfo(alias="updatedAt")
    """The date and time when the campaign was last updated, in ISO 8601 format."""
