# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from .emails_paging import EmailsPaging
from .public_campaign_asset import PublicCampaignAsset

__all__ = ["CollectionResponsePublicCampaignAsset"]


class CollectionResponsePublicCampaignAsset(BaseModel):
    results: List[PublicCampaignAsset]

    paging: Optional[EmailsPaging] = None
    """Contains information pagination of results."""
