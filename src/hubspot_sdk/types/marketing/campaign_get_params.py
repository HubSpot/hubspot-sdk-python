# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo

__all__ = ["CampaignGetParams"]


class CampaignGetParams(TypedDict, total=False):
    end_date: Annotated[str, PropertyInfo(alias="endDate")]
    """The end date for fetching asset metrics, in YYYY-MM-DD format. Optional.

    Example: 2000-01-27
    """

    properties: SequenceNotStr[str]
    """A comma-separated list of properties to include in the response.

    Unrecognized properties are ignored. Optional. Example: hs_name,hs_budget,
    hs_notes
    """

    start_date: Annotated[str, PropertyInfo(alias="startDate")]
    """The start date for fetching asset metrics, in YYYY-MM-DD format.

    Optional. Example: 2000-01-20
    """
