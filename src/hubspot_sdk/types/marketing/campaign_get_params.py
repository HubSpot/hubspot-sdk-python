# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo

__all__ = ["CampaignGetParams"]


class CampaignGetParams(TypedDict, total=False):
    end_date: Annotated[str, PropertyInfo(alias="endDate")]
    """The end date for filtering campaign data, in YYYY-MM-DD format."""

    properties: SequenceNotStr[str]
    """A comma-separated list of property names to include in the response."""

    start_date: Annotated[str, PropertyInfo(alias="startDate")]
    """The start date for filtering campaign data, in YYYY-MM-DD format."""
