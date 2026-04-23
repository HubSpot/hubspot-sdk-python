# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .limits_object_type_definition import LimitsObjectTypeDefinition

__all__ = ["AssociationLabelLimitResponse"]


class AssociationLabelLimitResponse(BaseModel):
    all_labels: List[str] = FieldInfo(alias="allLabels")
    """A list of all association labels."""

    from_object_type: LimitsObjectTypeDefinition = FieldInfo(alias="fromObjectType")

    limit: int
    """The maximum number of association labels allowed."""

    percentage: float
    """The percentage of the association label limit that has been used."""

    to_object_type: LimitsObjectTypeDefinition = FieldInfo(alias="toObjectType")

    usage: int
    """The current number of association labels used."""
