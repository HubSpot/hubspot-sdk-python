# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["PublicSequenceStepDependencyResponse"]


class PublicSequenceStepDependencyResponse(BaseModel):
    id: str

    created_at: datetime = FieldInfo(alias="createdAt")

    dependency_type: str = FieldInfo(alias="dependencyType")

    relies_on_sequence_step_id: str = FieldInfo(alias="reliesOnSequenceStepId")

    relies_on_step_order: int = FieldInfo(alias="reliesOnStepOrder")

    required_by_sequence_step_id: str = FieldInfo(alias="requiredBySequenceStepId")

    required_by_step_order: int = FieldInfo(alias="requiredByStepOrder")

    updated_at: datetime = FieldInfo(alias="updatedAt")
