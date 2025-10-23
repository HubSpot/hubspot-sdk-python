# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["APIEnumerationOutputField"]


class APIEnumerationOutputField(BaseModel):
    name: str

    options: List[str]

    type: Literal["ENUMERATION"]
