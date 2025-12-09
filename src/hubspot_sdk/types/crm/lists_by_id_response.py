# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List

from ..._models import BaseModel

__all__ = ["ListsByIDResponse"]


class ListsByIDResponse(BaseModel):
    """The response object containing the lists found for a multi-list fetch."""

    lists: List["PublicObjectList"]
    """The object list definitions."""


from .public_object_list import PublicObjectList
