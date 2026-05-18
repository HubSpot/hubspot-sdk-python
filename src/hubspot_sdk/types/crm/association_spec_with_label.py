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
    """Association category.

    Can be HUBSPOT_DEFINED, USER_DEFINED, INTEGRATOR_DEFINED or WORK
    """

    type_id: int = FieldInfo(alias="typeId")
    """
    An integer value used to uniquely identify a specific association type within
    its Association Category.
    """

    label: Optional[str] = None
    """
    An optional descriptor that provides additional context about the relationship
    between associated records, such as "Mentor" and "Mentee".
    """
