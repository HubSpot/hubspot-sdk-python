# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["AssociationSpec1"]


class AssociationSpec1(BaseModel):
    association_category: Literal["HUBSPOT_DEFINED", "USER_DEFINED", "INTEGRATOR_DEFINED"] = FieldInfo(
        alias="associationCategory"
    )
    """The category of the association, such as "HUBSPOT_DEFINED"."""

    association_type_id: int = FieldInfo(alias="associationTypeId")
    """The ID representing the specific type of association."""
