# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from ..shared.standard_error import StandardError
from .public_association_definition_configuration_update_result import (
    PublicAssociationDefinitionConfigurationUpdateResult,
)

__all__ = ["BatchResponsePublicAssociationDefinitionConfigurationUpdateResult"]


class BatchResponsePublicAssociationDefinitionConfigurationUpdateResult(BaseModel):
    completed_at: datetime = FieldInfo(alias="completedAt")
    """The date and time when the batch update operation was completed."""

    results: List[PublicAssociationDefinitionConfigurationUpdateResult]

    started_at: datetime = FieldInfo(alias="startedAt")
    """The date and time when the batch update operation started."""

    status: Literal["CANCELED", "COMPLETE", "PENDING", "PROCESSING"]
    """
    The current status of the batch update operation, which can be CANCELED,
    COMPLETE, PENDING, or PROCESSING.
    """

    errors: Optional[List[StandardError]] = None

    links: Optional[Dict[str, str]] = None
    """
    URLs linking to documentation or resources associated with the batch update
    operation.
    """

    num_errors: Optional[int] = FieldInfo(alias="numErrors", default=None)
    """The total number of errors encountered during the batch update operation."""

    requested_at: Optional[datetime] = FieldInfo(alias="requestedAt", default=None)
    """The date and time when the batch update operation was requested."""
