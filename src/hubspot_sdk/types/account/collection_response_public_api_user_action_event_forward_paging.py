# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from ..shared.forward_paging import ForwardPaging
from .public_api_user_action_event import PublicAPIUserActionEvent

__all__ = ["CollectionResponsePublicAPIUserActionEventForwardPaging"]


class CollectionResponsePublicAPIUserActionEventForwardPaging(BaseModel):
    results: List[PublicAPIUserActionEvent]

    paging: Optional[ForwardPaging] = None
