# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from ..shared.paging import Paging
from .public_campaign_asset import PublicCampaignAsset

__all__ = ["CollectionResponsePublicCampaignAsset"]


class CollectionResponsePublicCampaignAsset(BaseModel):
    results: List[PublicCampaignAsset]
    """An array of public campaign assets.

    Each item in the array is an object representing a campaign asset.
    """

    paging: Optional[Paging] = None
