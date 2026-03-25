# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from .public_campaign_asset import PublicCampaignAsset
from ..shared.forward_paging import ForwardPaging

__all__ = ["CollectionResponsePublicCampaignAssetForwardPaging"]


class CollectionResponsePublicCampaignAssetForwardPaging(BaseModel):
    results: List[PublicCampaignAsset]
    """An array of public campaign assets.

    Each item in the array is a reference to a PublicCampaignAsset object.
    """

    paging: Optional[ForwardPaging] = None
