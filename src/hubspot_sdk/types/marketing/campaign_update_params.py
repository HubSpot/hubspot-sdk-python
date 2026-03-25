# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Required, TypedDict

__all__ = ["CampaignUpdateParams"]


class CampaignUpdateParams(TypedDict, total=False):
    properties: Required[Dict[str, str]]
    """A collection of key-value pairs representing the properties of the campaign.

    Each key is a property name, and the corresponding value is the property's
    value.
    """
