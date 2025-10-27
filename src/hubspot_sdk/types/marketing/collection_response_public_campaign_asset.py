# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .paging import Paging
from ..._models import BaseModel
from .public_campaign_asset import PublicCampaignAsset

__all__ = ["CollectionResponsePublicCampaignAsset"]


class CollectionResponsePublicCampaignAsset(BaseModel):
    results: List[PublicCampaignAsset]

    paging: Optional[Paging] = None
    """Contains information pagination of results."""
