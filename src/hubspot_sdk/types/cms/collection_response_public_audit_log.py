# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from ..shared.paging import Paging
from .public_audit_log import PublicAuditLog

__all__ = ["CollectionResponsePublicAuditLog"]


class CollectionResponsePublicAuditLog(BaseModel):
    results: List[PublicAuditLog]

    paging: Optional[Paging] = None
