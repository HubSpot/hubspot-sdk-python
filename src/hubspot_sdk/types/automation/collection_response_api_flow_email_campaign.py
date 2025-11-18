# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from ..shared.paging import Paging
from .api_flow_email_campaign import APIFlowEmailCampaign

__all__ = ["CollectionResponseAPIFlowEmailCampaign"]


class CollectionResponseAPIFlowEmailCampaign(BaseModel):
    results: List[APIFlowEmailCampaign]

    paging: Optional[Paging] = None
