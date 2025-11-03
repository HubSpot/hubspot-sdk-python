# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from .public_import_response import PublicImportResponse
from ..marketing.emails_paging import EmailsPaging

__all__ = ["CollectionResponsePublicImportResponse"]


class CollectionResponsePublicImportResponse(BaseModel):
    results: List[PublicImportResponse]

    paging: Optional[EmailsPaging] = None
    """Contains information pagination of results."""
