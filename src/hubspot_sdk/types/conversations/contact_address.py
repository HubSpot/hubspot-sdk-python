# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["ContactAddress"]


class ContactAddress(BaseModel):
    city: Optional[str] = None

    country: Optional[str] = None

    country_code: Optional[str] = FieldInfo(alias="countryCode", default=None)

    state: Optional[str] = None

    street: Optional[str] = None

    type: Optional[Literal["HOME", "WORK"]] = None

    zip: Optional[str] = None
