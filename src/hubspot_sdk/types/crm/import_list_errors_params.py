# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["ImportListErrorsParams"]


class ImportListErrorsParams(TypedDict, total=False):
    after: str
    """
    The paging cursor token of the last successfully read resource will be returned
    as the `paging.next.after` JSON property of a paged response containing more
    results.
    """

    include_error_message: Annotated[bool, PropertyInfo(alias="includeErrorMessage")]
    """Set to True to receive a message explaining the error."""

    include_row_data: Annotated[bool, PropertyInfo(alias="includeRowData")]
    """Set to True to receive the data values for the errored row."""

    limit: int
    """The maximum number of results to display per page."""
