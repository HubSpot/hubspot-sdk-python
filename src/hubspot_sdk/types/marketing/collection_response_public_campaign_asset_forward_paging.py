# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from .public_campaign_asset import PublicCampaignAsset
from ..shared.forward_paging import ForwardPaging

__all__ = ["CollectionResponsePublicCampaignAssetForwardPaging"]


class CollectionResponsePublicCampaignAssetForwardPaging(BaseModel):
    results: List[PublicCampaignAsset]

    paging: Optional[ForwardPaging] = None
