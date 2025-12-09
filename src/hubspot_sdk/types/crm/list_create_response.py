# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ..._models import BaseModel

__all__ = ["ListCreateResponse"]


class ListCreateResponse(BaseModel):
    """The response for a list create request."""

    list: "PublicObjectList"
    """An object list definition."""


from .public_object_list import PublicObjectList
