# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["ClientCredentialsTokenResponse"]


class ClientCredentialsTokenResponse(BaseModel):
    access_token: str

    expires_in: int

    token_type: str

    token_use: Literal["client_credentials"]

    hub_id: Optional[int] = None

    id_token: Optional[str] = None

    scopes: Optional[List[str]] = None

    user_id: Optional[int] = None
