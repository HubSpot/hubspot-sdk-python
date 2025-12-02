# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from pydantic import Field as FieldInfo

from .group import Group
from ..._models import BaseModel
from .property_definition import PropertyDefinition
from .inbound_db_object_type import InboundDBObjectType

__all__ = ["IntegratorObjectCreationResponse"]


class IntegratorObjectCreationResponse(BaseModel):
    object_type: InboundDBObjectType = FieldInfo(alias="objectType")

    properties: List[PropertyDefinition]

    property_groups: List[Group] = FieldInfo(alias="propertyGroups")
