# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from .public_tax_rate_group import PublicTaxRateGroup
from ..shared.forward_paging import ForwardPaging

__all__ = ["CollectionResponsePublicTaxRateGroupForwardPaging"]


class CollectionResponsePublicTaxRateGroupForwardPaging(BaseModel):
    results: List[PublicTaxRateGroup]

    paging: Optional[ForwardPaging] = None
