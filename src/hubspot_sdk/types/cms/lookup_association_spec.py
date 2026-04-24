# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from ..shared.association_spec import AssociationSpec

__all__ = ["LookupAssociationSpec"]


class LookupAssociationSpec(BaseModel):
    association_spec: AssociationSpec = FieldInfo(alias="associationSpec")
    """
    Defines the type, direction, and details of the relationship between two CRM
    objects.
    """

    cardinality: Optional[Literal["ONE_TO_MANY", "ONE_TO_ONE"]] = None

    max_to_object_ids: Optional[int] = FieldInfo(alias="maxToObjectIds", default=None)

    to_object_type_id: Optional[str] = FieldInfo(alias="toObjectTypeId", default=None)
