# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from .public_audit_log import PublicAuditLog
from ..marketing.emails_paging import EmailsPaging

__all__ = ["CollectionResponsePublicAuditLog"]


class CollectionResponsePublicAuditLog(BaseModel):
    results: List[PublicAuditLog]

    paging: Optional[EmailsPaging] = None
    """Contains information pagination of results."""
