# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

from ..public_campaign_batch_update_item_param import PublicCampaignBatchUpdateItemParam

__all__ = ["BatchUpdateParams"]


class BatchUpdateParams(TypedDict, total=False):
    inputs: Required[Iterable[PublicCampaignBatchUpdateItemParam]]
    """
    An array of PublicCampaignBatchUpdateItem objects, each containing the ID and
    properties to update for a specific campaign.
    """
