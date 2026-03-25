# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from .public_email import PublicEmail
from ..shared.paging import Paging

__all__ = ["CollectionResponseWithTotalPublicEmail"]


class CollectionResponseWithTotalPublicEmail(BaseModel):
    results: List[PublicEmail]

    total: int

    paging: Optional[Paging] = None
