# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo

__all__ = ["EmailGetAbTestVariationParams"]


class EmailGetAbTestVariationParams(TypedDict, total=False):
    archived: bool
    """Boolean variable to request archived email"""

    included_properties: Annotated[SequenceNotStr[str], PropertyInfo(alias="includedProperties")]
    """List of properties to be returned in the API response"""

    include_stats: Annotated[bool, PropertyInfo(alias="includeStats")]
    """Boolean variable to request stats to be returned in response"""

    marketing_campaign_names: Annotated[bool, PropertyInfo(alias="marketingCampaignNames")]
    """Boolean variable to request name of the campaign in response"""

    workflow_names: Annotated[bool, PropertyInfo(alias="workflowNames")]
    """Boolean variable to request name of the associated workflows in response"""
