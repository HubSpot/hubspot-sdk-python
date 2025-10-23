# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from ..shared.forward_paging import ForwardPaging
from .public_action_definition import PublicActionDefinition

__all__ = ["CollectionResponsePublicActionDefinitionForwardPaging"]


class CollectionResponsePublicActionDefinitionForwardPaging(BaseModel):
    results: List[PublicActionDefinition]

    paging: Optional[ForwardPaging] = None
