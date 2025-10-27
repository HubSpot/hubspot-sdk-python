# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

from ..._types import SequenceNotStr

__all__ = ["CampaignListParams"]


class CampaignListParams(TypedDict, total=False):
    after: str
    """A cursor for pagination.

    If provided, the results will start after the given cursor. Example:
    NTI1Cg%3D%3D
    """

    limit: int
    """The maximum number of results to return.

    Allowed values range from 1 to 100 Default: 50
    """

    name: str
    """A filter to return campaigns whose names contain the specified substring.

    This allows partial matching of campaign names, returning all campaigns that
    include the given substring in their name. If this parameter is not provided,
    the search will return all campaigns
    """

    properties: SequenceNotStr[str]
    """A comma-separated list of the properties to be returned in the response.

    If any of the specified properties has empty value on the requested object(s),
    they will be ignored and not returned in response. If this parameter is empty,
    the response will include an empty properties map
    """

    sort: str
    """The field by which to sort the results.

    Allowed values are hs_name, createdAt, updatedAt. An optional '-' before the
    property name can denote descending order Default: hs_name
    """
