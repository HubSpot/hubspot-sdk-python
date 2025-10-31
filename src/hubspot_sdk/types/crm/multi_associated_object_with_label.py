# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .association_spec_with_label import AssociationSpecWithLabel

__all__ = ["MultiAssociatedObjectWithLabel"]


class MultiAssociatedObjectWithLabel(BaseModel):
    association_types: List[AssociationSpecWithLabel] = FieldInfo(alias="associationTypes")

    to_object_id: str = FieldInfo(alias="toObjectId")
