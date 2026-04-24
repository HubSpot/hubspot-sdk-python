# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["PublicRefreshTokenInfoResponse"]


class PublicRefreshTokenInfoResponse(BaseModel):
    token: str

    active: bool

    app_id: int

    client_id: str

    hub_id: int

    scopes: List[str]

    token_type: str

    token_use: Literal["refresh_token"]

    user_id: int

    hub_domain: Optional[str] = None

    user: Optional[str] = None
