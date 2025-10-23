# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["ExternalUserProfile"]


class ExternalUserProfile(BaseModel):
    email: str

    first_name: Optional[str] = FieldInfo(alias="firstName", default=None)

    full_name: Optional[str] = FieldInfo(alias="fullName", default=None)

    last_name: Optional[str] = FieldInfo(alias="lastName", default=None)
