# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .ip_range import IPRange
from ..._models import BaseModel

__all__ = ["CollectionResponseIPRangeNoPaging"]


class CollectionResponseIPRangeNoPaging(BaseModel):
    results: List[IPRange]
    """
    An array of IpRange objects, each representing a specific IP range with
    associated details such as CIDR, direction, service, and description.
    """
