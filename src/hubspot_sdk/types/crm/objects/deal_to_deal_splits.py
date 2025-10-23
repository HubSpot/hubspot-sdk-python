# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ...._models import BaseModel
from ..simple_public_object import SimplePublicObject

__all__ = ["DealToDealSplits"]


class DealToDealSplits(BaseModel):
    id: str

    splits: List[SimplePublicObject]
