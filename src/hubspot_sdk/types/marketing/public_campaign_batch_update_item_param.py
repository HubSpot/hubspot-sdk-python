# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Required, TypedDict

__all__ = ["PublicCampaignBatchUpdateItemParam"]


class PublicCampaignBatchUpdateItemParam(TypedDict, total=False):
    id: Required[str]
    """The unique identifier for the campaign to be updated. It is a string."""

    properties: Required[Dict[str, str]]
    """A map of property names to their new values for the campaign.

    Each property name is a string, and its value is also a string.
    """
