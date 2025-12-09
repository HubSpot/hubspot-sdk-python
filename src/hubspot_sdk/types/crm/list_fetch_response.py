# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ..._models import BaseModel

__all__ = ["ListFetchResponse"]


class ListFetchResponse(BaseModel):
    """The response for a list fetch request."""

    list: "PublicObjectList"
    """An object list definition."""


from .public_object_list import PublicObjectList
