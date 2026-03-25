# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["AssociationDefinitionEgg"]


class AssociationDefinitionEgg(BaseModel):
    from_object_type_id: str = FieldInfo(alias="fromObjectTypeId")

    to_object_type_id: str = FieldInfo(alias="toObjectTypeId")

    name: Optional[str] = None
