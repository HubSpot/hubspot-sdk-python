# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .public_sequence_step_response import PublicSequenceStepResponse
from .public_sequence_settings_response import PublicSequenceSettingsResponse
from .public_sequence_step_dependency_response import PublicSequenceStepDependencyResponse

__all__ = ["PublicSequenceResponse"]


class PublicSequenceResponse(BaseModel):
    id: str
    """The unique identifier for the sequence."""

    created_at: datetime = FieldInfo(alias="createdAt")
    """The date and time when the sequence was created."""

    dependencies: List[PublicSequenceStepDependencyResponse]
    """
    An array of dependencies for the sequence steps, each represented as a
    PublicSequenceStepDependencyResponse object.
    """

    name: str
    """The name of the sequence."""

    steps: List[PublicSequenceStepResponse]
    """
    An array of steps included in the sequence, each represented by a
    PublicSequenceStepResponse object.
    """

    updated_at: datetime = FieldInfo(alias="updatedAt")
    """The date and time when the sequence was last updated."""

    user_id: str = FieldInfo(alias="userId")
    """The ID of the user associated with the sequence."""

    folder_id: Optional[str] = FieldInfo(alias="folderId", default=None)
    """The identifier of the folder containing the sequence."""

    settings: Optional[PublicSequenceSettingsResponse] = None
