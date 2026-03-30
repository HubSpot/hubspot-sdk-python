# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from ..shared.standard_error import StandardError
from .public_campaign_with_assets import PublicCampaignWithAssets

__all__ = ["BatchResponsePublicCampaignWithAssets"]


class BatchResponsePublicCampaignWithAssets(BaseModel):
    completed_at: datetime = FieldInfo(alias="completedAt")
    """The timestamp when the batch request processing was completed."""

    results: List[PublicCampaignWithAssets]
    """
    An array of results from the batch operation, each representing a public
    campaign with assets.
    """

    started_at: datetime = FieldInfo(alias="startedAt")
    """The timestamp when the processing of the batch request began."""

    status: Literal["CANCELED", "COMPLETE", "PENDING", "PROCESSING"]
    """
    The current processing status of the batch operation, with possible values:
    CANCELED, COMPLETE, PENDING, PROCESSING.
    """

    errors: Optional[List[StandardError]] = None
    """
    An array of errors encountered during the batch operation, each described by a
    StandardError object.
    """

    links: Optional[Dict[str, str]] = None
    """A collection of URLs linking to related resources or documentation."""

    num_errors: Optional[int] = FieldInfo(alias="numErrors", default=None)
    """The number of errors encountered during the batch operation."""

    requested_at: Optional[datetime] = FieldInfo(alias="requestedAt", default=None)
    """The timestamp when the batch request was initially made."""
