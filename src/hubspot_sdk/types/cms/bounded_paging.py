# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel
from .bounded_next_page import BoundedNextPage

__all__ = ["BoundedPaging"]


class BoundedPaging(BaseModel):
    next: Optional[BoundedNextPage] = None
