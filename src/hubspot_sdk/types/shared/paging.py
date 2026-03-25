# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel
from .next_page import NextPage
from .previous_page import PreviousPage

__all__ = ["Paging"]


class Paging(BaseModel):
    next: Optional[NextPage] = None
    """
    Specifies the paging information needed to retrieve the next set of results in a
    paginated API response
    """

    prev: Optional[PreviousPage] = None
    """
    specifies the paging information needed to retrieve the previous set of results
    in a paginated API response
    """
