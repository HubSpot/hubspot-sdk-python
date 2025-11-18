# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo

__all__ = ["CustomChannelListParams"]


class CustomChannelListParams(TypedDict, total=False):
    after: str
    """
    The paging cursor token of the last successfully read resource will be returned
    as the `paging.next.after` JSON property of a paged response containing more
    results.
    """

    default_page_length: Annotated[int, PropertyInfo(alias="defaultPageLength")]
    """Specify the default number of results to return per page."""

    limit: int
    """The maximum number of results to display per page."""

    sort: SequenceNotStr[str]
    """Specify the sorting order for the results."""
