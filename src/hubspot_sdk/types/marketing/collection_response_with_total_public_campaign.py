# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from ..shared.paging import Paging
from .public_campaign import PublicCampaign

__all__ = ["CollectionResponseWithTotalPublicCampaign"]


class CollectionResponseWithTotalPublicCampaign(BaseModel):
    results: List[PublicCampaign]
    """
    An array of PublicCampaign objects, each representing a campaign with its
    associated properties.
    """

    total: int
    """An integer representing the total number of public campaigns available."""

    paging: Optional[Paging] = None
