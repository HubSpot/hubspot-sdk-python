# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo

__all__ = ["EmailGetParams"]


class EmailGetParams(TypedDict, total=False):
    archived: bool
    """Whether to return only results that have been archived."""

    included_properties: Annotated[SequenceNotStr[str], PropertyInfo(alias="includedProperties")]
    """Limit the response to only include the specified properties."""

    include_stats: Annotated[bool, PropertyInfo(alias="includeStats")]
    """Include statistics with email."""

    marketing_campaign_names: Annotated[bool, PropertyInfo(alias="marketingCampaignNames")]
    """If set to true, loads `campaignName` and `campaignUtm`."""

    workflow_names: Annotated[bool, PropertyInfo(alias="workflowNames")]
    """
    If set to true, loads workflows in which the email is used within a "send email"
    action.
    """
