# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel
from .public_audit_info import PublicAuditInfo

__all__ = ["CollectionResponsePublicAuditInfoNoPaging"]


class CollectionResponsePublicAuditInfoNoPaging(BaseModel):
    results: List[PublicAuditInfo]
