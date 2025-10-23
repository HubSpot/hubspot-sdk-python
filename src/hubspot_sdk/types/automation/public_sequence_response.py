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

    created_at: datetime = FieldInfo(alias="createdAt")

    dependencies: List[PublicSequenceStepDependencyResponse]

    name: str

    steps: List[PublicSequenceStepResponse]

    updated_at: datetime = FieldInfo(alias="updatedAt")

    user_id: str = FieldInfo(alias="userId")

    folder_id: Optional[str] = FieldInfo(alias="folderId", default=None)

    settings: Optional[PublicSequenceSettingsResponse] = None
