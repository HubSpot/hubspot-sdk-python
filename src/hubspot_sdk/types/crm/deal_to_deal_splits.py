# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel
from .simple_public_object import SimplePublicObject

__all__ = ["DealToDealSplits"]


class DealToDealSplits(BaseModel):
    id: str
    """The unique identifier for the deal associated with the deal splits."""

    splits: List[SimplePublicObject]
    """
    An array of deal split objects, each representing a portion of the deal assigned
    to an owner.
    """
