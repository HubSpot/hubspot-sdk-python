# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, Annotated, TypedDict

from ...._types import SequenceNotStr
from ...._utils import PropertyInfo
from ..public_campaign_read_input_param import PublicCampaignReadInputParam

__all__ = ["BatchGetParams"]


class BatchGetParams(TypedDict, total=False):
    inputs: Required[Iterable[PublicCampaignReadInputParam]]
    """
    An array of PublicCampaignReadInput objects, each containing the ID of a
    campaign to be read. This property is required.
    """

    end_date: Annotated[str, PropertyInfo(alias="endDate")]
    """The end date for filtering campaigns, in YYYY-MM-DD format."""

    properties: SequenceNotStr[str]
    """A comma-separated list of property names to include in the response."""

    start_date: Annotated[str, PropertyInfo(alias="startDate")]
    """The start date for filtering campaigns, in YYYY-MM-DD format."""
