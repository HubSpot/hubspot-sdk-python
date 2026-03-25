# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .group_view import GroupView
from .inbound_db_object_type import InboundDBObjectType

__all__ = ["ObjectDefinitionResponse"]


class ObjectDefinitionResponse(BaseModel):
    object_type_id: str = FieldInfo(alias="objectTypeId")

    object_type_name: str = FieldInfo(alias="objectTypeName")

    properties: List["PropertyDefinition"]

    property_groups: List[GroupView] = FieldInfo(alias="propertyGroups")

    schema_: Optional[InboundDBObjectType] = FieldInfo(alias="schema", default=None)


from .property_definition import PropertyDefinition
