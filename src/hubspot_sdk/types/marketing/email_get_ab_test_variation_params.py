# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo

__all__ = ["EmailGetAbTestVariationParams"]


class EmailGetAbTestVariationParams(TypedDict, total=False):
    archived: bool
    """Whether to return only results that have been archived."""

    included_properties: Annotated[SequenceNotStr[str], PropertyInfo(alias="includedProperties")]

    include_stats: Annotated[bool, PropertyInfo(alias="includeStats")]

    marketing_campaign_names: Annotated[bool, PropertyInfo(alias="marketingCampaignNames")]

    variant_stats: Annotated[bool, PropertyInfo(alias="variantStats")]

    workflow_names: Annotated[bool, PropertyInfo(alias="workflowNames")]
