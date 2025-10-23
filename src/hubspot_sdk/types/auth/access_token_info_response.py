# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["AccessTokenInfoResponse"]


class AccessTokenInfoResponse(BaseModel):
    token: str

    app_id: int

    expires_in: int

    hub_id: int

    scopes: List[str]

    token_type: str

    user_id: int

    hub_domain: Optional[str] = None

    user: Optional[str] = None
