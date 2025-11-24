# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["TokenResponseIf"]


class TokenResponseIf(BaseModel):
    access_token: Optional[str] = FieldInfo(alias="accessToken", default=None)

    expires_in: Optional[int] = FieldInfo(alias="expiresIn", default=None)

    hub_id: Optional[int] = FieldInfo(alias="hubId", default=None)

    id_token: Optional[str] = FieldInfo(alias="idToken", default=None)

    scopes: Optional[List[str]] = None

    token_type: Optional[str] = FieldInfo(alias="tokenType", default=None)

    user_id: Optional[int] = FieldInfo(alias="userId", default=None)
