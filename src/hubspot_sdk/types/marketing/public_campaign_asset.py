# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional

from ..._models import BaseModel

__all__ = ["PublicCampaignAsset"]


class PublicCampaignAsset(BaseModel):
    id: str
    """The unique identifier for the campaign asset."""

    metrics: Optional[Dict[str, float]] = None
    """
    A collection of metrics associated with the campaign asset, represented as
    key-value pairs.
    """

    name: Optional[str] = None
    """The name of the campaign asset."""
