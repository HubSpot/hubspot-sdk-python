# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

from ..._types import SequenceNotStr

__all__ = ["CampaignListParams"]


class CampaignListParams(TypedDict, total=False):
    after: str
    """
    The paging cursor token of the last successfully read resource will be returned
    as the `paging.next.after` JSON property of a paged response containing more
    results.
    """

    limit: int
    """The maximum number of results to display per page."""

    name: str
    """Filter campaigns by name. Optional."""

    properties: SequenceNotStr[str]
    """A comma-separated list of properties to include in the response.

    Unrecognized properties are ignored. Optional. Example:
     hs_name, hs_budget,hs_notes
    """

    sort: str
    """The property to sort results by. Optional."""
