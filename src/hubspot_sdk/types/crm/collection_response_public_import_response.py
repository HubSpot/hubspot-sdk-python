# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from ..shared.paging import Paging
from .public_import_response import PublicImportResponse

__all__ = ["CollectionResponsePublicImportResponse"]


class CollectionResponsePublicImportResponse(BaseModel):
    results: List[PublicImportResponse]

    paging: Optional[Paging] = None
