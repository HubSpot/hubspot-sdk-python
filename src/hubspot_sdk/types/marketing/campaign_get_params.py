# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo

__all__ = ["CampaignGetParams"]


class CampaignGetParams(TypedDict, total=False):
    end_date: Annotated[str, PropertyInfo(alias="endDate")]
    """End date to fetch asset metrics, formatted as YYYY-MM-DD.

    This date is used to fetch the metrics associated with the assets for a
    specified period. If not provided, no asset metrics will be fetched.
    """

    properties: SequenceNotStr[str]
    """A comma-separated list of the properties to be returned in the response.

    If any of the specified properties has empty value on the requested object, they
    will be ignored and not returned in response. If this parameter is empty, the
    response will include an empty properties map.
    """

    start_date: Annotated[str, PropertyInfo(alias="startDate")]
    """Start date to fetch asset metrics, formatted as YYYY-MM-DD.

    This date is used to fetch the metrics associated with the assets for a
    specified period. If not provided, no asset metrics will be fetched.
    """
