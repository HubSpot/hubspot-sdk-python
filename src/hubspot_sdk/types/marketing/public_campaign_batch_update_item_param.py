# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Required, TypedDict

__all__ = ["PublicCampaignBatchUpdateItemParam"]


class PublicCampaignBatchUpdateItemParam(TypedDict, total=False):
    id: Required[str]
    """The unique identifier for the campaign to be updated."""

    properties: Required[Dict[str, str]]
    """
    A set of key-value pairs representing the properties to be updated for the
    campaign.
    """
