# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["AssociationSpecWithLabel"]


class AssociationSpecWithLabel(BaseModel):
    category: Literal["HUBSPOT_DEFINED", "INTEGRATOR_DEFINED", "USER_DEFINED"]

    type_id: int = FieldInfo(alias="typeId")

    label: Optional[str] = None
