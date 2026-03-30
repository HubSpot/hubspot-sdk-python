# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from .smtp_api_token_view import SmtpAPITokenView
from ..shared.forward_paging import ForwardPaging

__all__ = ["CollectionResponseSmtpAPITokenViewForwardPaging"]


class CollectionResponseSmtpAPITokenViewForwardPaging(BaseModel):
    results: List[SmtpAPITokenView]

    paging: Optional[ForwardPaging] = None
