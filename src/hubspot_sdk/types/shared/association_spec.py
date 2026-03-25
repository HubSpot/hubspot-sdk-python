# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["AssociationSpec"]


class AssociationSpec(BaseModel):
    """
    Defines the type, direction, and details of the relationship between two CRM objects.
    """

    association_category: Literal["HUBSPOT_DEFINED", "INTEGRATOR_DEFINED", "USER_DEFINED", "WORK"] = FieldInfo(
        alias="associationCategory"
    )
    """The category of the association, such as "HUBSPOT_DEFINED"."""

    association_type_id: int = FieldInfo(alias="associationTypeId")
    """The ID representing the specific type of association."""
