# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel
from .api_usage import APIUsage

__all__ = ["CollectionResponseAPIUsageNoPaging"]


class CollectionResponseAPIUsageNoPaging(BaseModel):
    results: List[APIUsage]
