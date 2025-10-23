# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["PublicLocation"]


class PublicLocation(BaseModel):
    latitude: float

    longitude: float

    type: Literal["LOCATION"]

    address: Optional[str] = None

    name: Optional[str] = None

    url: Optional[str] = None
