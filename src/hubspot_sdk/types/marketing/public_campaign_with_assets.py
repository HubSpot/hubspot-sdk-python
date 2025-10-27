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

    assets: Dict[str, CollectionResponsePublicCampaignAsset]

    business_units: List[PublicBusinessUnit] = FieldInfo(alias="businessUnits")

    created_at: datetime = FieldInfo(alias="createdAt")

    properties: Dict[str, str]

    updated_at: datetime = FieldInfo(alias="updatedAt")
