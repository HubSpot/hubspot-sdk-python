# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from .public_login_audit import PublicLoginAudit
from ..shared.forward_paging import ForwardPaging

__all__ = ["CollectionResponsePublicLoginAuditForwardPaging"]


class CollectionResponsePublicLoginAuditForwardPaging(BaseModel):
    results: List[PublicLoginAudit]

    paging: Optional[ForwardPaging] = None
