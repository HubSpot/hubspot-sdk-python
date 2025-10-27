# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .objects.object_type_definition import ObjectTypeDefinition

__all__ = ["AssociationLabelLimitResponse"]


class AssociationLabelLimitResponse(BaseModel):
    all_labels: List[str] = FieldInfo(alias="allLabels")

    from_object_type: ObjectTypeDefinition = FieldInfo(alias="fromObjectType")
    """Defines an object type."""

    limit: int

    percentage: float

    to_object_type: ObjectTypeDefinition = FieldInfo(alias="toObjectType")
    """Defines an object type."""

    usage: int
