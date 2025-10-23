# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["ContactName"]


class ContactName(BaseModel):
    first_name: Optional[str] = FieldInfo(alias="firstName", default=None)

    last_name: Optional[str] = FieldInfo(alias="lastName", default=None)

    middle_name: Optional[str] = FieldInfo(alias="middleName", default=None)

    prefix: Optional[str] = None

    suffix: Optional[str] = None
