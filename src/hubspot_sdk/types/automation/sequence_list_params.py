# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["SequenceListParams"]


class SequenceListParams(TypedDict, total=False):
    user_id: Required[Annotated[str, PropertyInfo(alias="userId")]]
    """The unique identifier of the user whose sequences are to be retrieved.

    This parameter is required.
    """

    after: str
    """The paging cursor token of the last successfully read resource.

    Use this for pagination to retrieve the next set of results.
    """

    limit: int
    """The maximum number of results to display per page."""

    name: str
    """The name of the sequence to filter results by."""
