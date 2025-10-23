# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["MembershipListParams"]


class MembershipListParams(TypedDict, total=False):
    after: str
    """
    The paging offset token for the page that comes `after` the previously requested
    records.

    If provided, then the records in the response will be the records following the
    offset, sorted in _ascending_ order. Takes precedence over the `before` offset.
    """

    before: str
    """
    The paging offset token for the page that comes `before` the previously
    requested records.

    If provided, then the records in the response will be the records preceding the
    offset, sorted in _descending_ order.
    """

    limit: int
    """The number of records to return in the response. The maximum `limit` is 250."""
