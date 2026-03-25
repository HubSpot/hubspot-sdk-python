# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["AssociationSpecWithLabel"]


class AssociationSpecWithLabel(BaseModel):
    """
    Defines the type, direction, and details of the relationship between two CRM objects.
    """

    category: Literal["HUBSPOT_DEFINED", "INTEGRATOR_DEFINED", "USER_DEFINED", "WORK"]
    """
    The category of the association, such as HUBSPOT_DEFINED, USER_DEFINED, or
    INTEGRATOR_DEFINED.
    """

    type_id: int = FieldInfo(alias="typeId")
    """The unique identifier for the type of association."""

    label: Optional[str] = None
    """A label describing the association between two objects."""
