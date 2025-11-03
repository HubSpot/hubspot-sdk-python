# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from .api_flow_email_campaign import APIFlowEmailCampaign
from ..marketing.emails_paging import EmailsPaging

__all__ = ["CollectionResponseAPIFlowEmailCampaign"]


class CollectionResponseAPIFlowEmailCampaign(BaseModel):
    results: List[APIFlowEmailCampaign]

    paging: Optional[EmailsPaging] = None
    """Contains information pagination of results."""
