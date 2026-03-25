# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from ..shared.forward_paging import ForwardPaging
from .public_import_response import PublicImportResponse

__all__ = ["CollectionResponsePublicImportResponseForwardPaging"]


class CollectionResponsePublicImportResponseForwardPaging(BaseModel):
    results: List[PublicImportResponse]

    paging: Optional[ForwardPaging] = None
