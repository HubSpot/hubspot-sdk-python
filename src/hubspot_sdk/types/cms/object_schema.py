# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .property_1 import Property1
from ..shared.association_definition import AssociationDefinition
from ..shared.object_type_definition_labels import ObjectTypeDefinitionLabels

__all__ = ["ObjectSchema"]


class ObjectSchema(BaseModel):
    id: str

    allows_sensitive_properties: bool = FieldInfo(alias="allowsSensitiveProperties")

    archived: bool

    associations: List[AssociationDefinition]

    fully_qualified_name: str = FieldInfo(alias="fullyQualifiedName")

    labels: ObjectTypeDefinitionLabels

    name: str

    object_type_id: str = FieldInfo(alias="objectTypeId")

    properties: List[Property1]

    required_properties: List[str] = FieldInfo(alias="requiredProperties")

    searchable_properties: List[str] = FieldInfo(alias="searchableProperties")

    secondary_display_properties: List[str] = FieldInfo(alias="secondaryDisplayProperties")

    created_at: Optional[datetime] = FieldInfo(alias="createdAt", default=None)

    created_by_user_id: Optional[int] = FieldInfo(alias="createdByUserId", default=None)

    description: Optional[str] = None

    primary_display_property: Optional[str] = FieldInfo(alias="primaryDisplayProperty", default=None)

    updated_at: Optional[datetime] = FieldInfo(alias="updatedAt", default=None)

    updated_by_user_id: Optional[int] = FieldInfo(alias="updatedByUserId", default=None)
