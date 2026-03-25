# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["PreviousPage"]


class PreviousPage(BaseModel):
    """
    specifies the paging information needed to retrieve the previous set of results in a paginated API response
    """

    before: str
    """
    A string token used to identify the position before the current page in the
    pagination sequence.
    """

    link: Optional[str] = None
    """A URL string that provides a direct link to the previous page of results."""
