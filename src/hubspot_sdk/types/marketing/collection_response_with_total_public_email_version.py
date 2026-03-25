# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from ..shared.paging import Paging
from .version_public_email import VersionPublicEmail

__all__ = ["CollectionResponseWithTotalPublicEmailVersion"]


class CollectionResponseWithTotalPublicEmailVersion(BaseModel):
    results: List[VersionPublicEmail]

    total: int

    paging: Optional[Paging] = None
