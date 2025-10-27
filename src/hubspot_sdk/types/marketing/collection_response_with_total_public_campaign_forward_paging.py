# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from .public_campaign import PublicCampaign
from ..shared.forward_paging import ForwardPaging

__all__ = ["CollectionResponseWithTotalPublicCampaignForwardPaging"]


class CollectionResponseWithTotalPublicCampaignForwardPaging(BaseModel):
    results: List[PublicCampaign]

    total: int

    paging: Optional[ForwardPaging] = None
