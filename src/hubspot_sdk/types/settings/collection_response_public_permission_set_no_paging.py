# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel
from .public_permission_set import PublicPermissionSet

__all__ = ["CollectionResponsePublicPermissionSetNoPaging"]


class CollectionResponsePublicPermissionSetNoPaging(BaseModel):
    results: List[PublicPermissionSet]
