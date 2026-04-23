# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ..._models import BaseModel
from .signed_access_token import SignedAccessToken

__all__ = ["PublicAccessTokenInfoResponse"]


class PublicAccessTokenInfoResponse(BaseModel):
    token: str

    active: bool

    app_id: int

    client_id: str

    expires_in: int

    hub_id: int

    is_private_distribution: bool

    scopes: List[str]

    signed_access_token: SignedAccessToken

    token_type: str

    token_use: Literal["access_token"]

    user_id: int

    hub_domain: Optional[str] = None

    user: Optional[str] = None
