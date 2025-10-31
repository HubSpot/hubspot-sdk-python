# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["APIAssociationTimestampDataSource"]


class APIAssociationTimestampDataSource(BaseModel):
    association_category: Literal["HUBSPOT_DEFINED", "USER_DEFINED", "INTEGRATOR_DEFINED"] = FieldInfo(
        alias="associationCategory"
    )

    association_type_id: int = FieldInfo(alias="associationTypeId")
    """The ID representing the type of association."""

    name: str

    object_type_id: str = FieldInfo(alias="objectTypeId")

    type: Literal["ASSOCIATION_TIMESTAMP"]
