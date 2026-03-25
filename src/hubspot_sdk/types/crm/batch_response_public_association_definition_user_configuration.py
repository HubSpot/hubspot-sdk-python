# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from ..shared.standard_error import StandardError
from .public_association_definition_user_configuration import PublicAssociationDefinitionUserConfiguration

__all__ = ["BatchResponsePublicAssociationDefinitionUserConfiguration"]


class BatchResponsePublicAssociationDefinitionUserConfiguration(BaseModel):
    completed_at: datetime = FieldInfo(alias="completedAt")
    """The date and time when the batch operation was completed."""

    results: List[PublicAssociationDefinitionUserConfiguration]

    started_at: datetime = FieldInfo(alias="startedAt")
    """The date and time when the batch operation started."""

    status: Literal["CANCELED", "COMPLETE", "PENDING", "PROCESSING"]
    """
    The current status of the batch operation, which can be CANCELED, COMPLETE,
    PENDING, or PROCESSING.
    """

    errors: Optional[List[StandardError]] = None

    links: Optional[Dict[str, str]] = None
    """
    A collection of URLs linking to related documentation or resources associated
    with the batch operation.
    """

    num_errors: Optional[int] = FieldInfo(alias="numErrors", default=None)
    """The total number of errors encountered during the batch operation."""

    requested_at: Optional[datetime] = FieldInfo(alias="requestedAt", default=None)
    """The date and time when the batch operation was requested."""
