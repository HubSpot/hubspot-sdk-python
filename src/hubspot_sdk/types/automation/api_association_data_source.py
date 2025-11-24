# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .api_sort import APISort
from ..._models import BaseModel

__all__ = ["APIAssociationDataSource"]


class APIAssociationDataSource(BaseModel):
    association_category: Literal["HUBSPOT_DEFINED", "INTEGRATOR_DEFINED", "USER_DEFINED"] = FieldInfo(
        alias="associationCategory"
    )

    association_type_id: int = FieldInfo(alias="associationTypeId")

    name: str

    object_type_id: str = FieldInfo(alias="objectTypeId")

    type: Literal["ASSOCIATION"]

    sort_by: Optional[APISort] = FieldInfo(alias="sortBy", default=None)
