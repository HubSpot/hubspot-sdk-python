# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from .public_import_error import PublicImportError
from ..shared.forward_paging import ForwardPaging

__all__ = ["CollectionResponsePublicImportErrorForwardPaging"]


class CollectionResponsePublicImportErrorForwardPaging(BaseModel):
    results: List[PublicImportError]

    paging: Optional[ForwardPaging] = None
