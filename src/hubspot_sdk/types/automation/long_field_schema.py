# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["LongFieldSchema"]


class LongFieldSchema(BaseModel):
    type: Literal["LONG"]

    maximum: Optional[int] = None

    minimum: Optional[int] = None
