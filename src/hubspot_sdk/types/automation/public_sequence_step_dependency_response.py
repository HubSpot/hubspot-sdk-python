# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["PublicSequenceStepDependencyResponse"]


class PublicSequenceStepDependencyResponse(BaseModel):
    id: str
    """The unique identifier of the step dependency."""

    created_at: datetime = FieldInfo(alias="createdAt")
    """The date and time when the step dependency was created."""

    dependency_type: Literal["MANUAL_PAUSE", "TASK_COMPLETION"] = FieldInfo(alias="dependencyType")
    """
    The type of dependency between sequence steps with accepted values being
    TASK_COMPLETION or MANUAL_PAUSE.
    """

    relies_on_sequence_step_id: str = FieldInfo(alias="reliesOnSequenceStepId")
    """
    The unique identifier of the sequence step that is responsible for creating and
    resolving this dependency.
    """

    relies_on_step_order: int = FieldInfo(alias="reliesOnStepOrder")
    """
    The order number of the step that is responsible for creating and resolving this
    dependency.
    """

    required_by_sequence_step_id: str = FieldInfo(alias="requiredBySequenceStepId")
    """The unique identifier of the sequence step that requires this dependency."""

    required_by_step_order: int = FieldInfo(alias="requiredByStepOrder")
    """The order number of the step that requires this dependency."""

    updated_at: datetime = FieldInfo(alias="updatedAt")
    """The date and time when the step dependency was last updated."""
