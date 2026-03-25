# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["PreviousPage"]


class PreviousPage(BaseModel):
    """
    specifies the paging information needed to retrieve the previous set of results in a paginated API response
    """

    before: str
    """A paging cursor token for retrieving previous pages."""

    link: Optional[str] = None
    """A URL that can be used to retrieve the previous pages' results."""
