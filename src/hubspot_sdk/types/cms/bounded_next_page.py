# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["BoundedNextPage"]


class BoundedNextPage(BaseModel):
    offset: int
    """The offset value indicating the starting point for the next set of results."""

    link: Optional[str] = None
    """A URL that can be used to retrieve the next set of results."""
