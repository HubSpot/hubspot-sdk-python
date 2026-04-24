# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from ..shared.base_property import BaseProperty
from ..shared.base_association_definition import BaseAssociationDefinition
from ..shared.object_type_definition_labels import ObjectTypeDefinitionLabels

__all__ = ["ObjectSchema"]


class ObjectSchema(BaseModel):
    id: str
    """A unique ID for this schema's object type.

    Will be defined as {meta-type}-{unique ID}.
    """

    allows_sensitive_properties: bool = FieldInfo(alias="allowsSensitiveProperties")

    archived: bool

    associations: List[BaseAssociationDefinition]
    """Associations defined for a given object type."""

    fully_qualified_name: str = FieldInfo(alias="fullyQualifiedName")
    """An assigned unique ID for the object, including portal ID and object name."""

    labels: ObjectTypeDefinitionLabels

    name: str
    """A unique name for the schema's object type."""

    object_type_id: str = FieldInfo(alias="objectTypeId")

    properties: List[BaseProperty]
    """Properties defined for this object type."""

    required_properties: List[str] = FieldInfo(alias="requiredProperties")
    """
    The names of properties that should be **required** when creating an object of
    this type.
    """

    searchable_properties: List[str] = FieldInfo(alias="searchableProperties")
    """
    Names of properties that will be indexed for this object type in by HubSpot's
    product search.
    """

    secondary_display_properties: List[str] = FieldInfo(alias="secondaryDisplayProperties")
    """The names of secondary properties for this object.

    These will be displayed as secondary on the HubSpot record page for this object
    type.
    """

    created_at: Optional[datetime] = FieldInfo(alias="createdAt", default=None)
    """When the object schema was created."""

    created_by_user_id: Optional[int] = FieldInfo(alias="createdByUserId", default=None)

    description: Optional[str] = None

    primary_display_property: Optional[str] = FieldInfo(alias="primaryDisplayProperty", default=None)
    """The name of the primary property for this object.

    This will be displayed as primary on the HubSpot record page for this object
    type.
    """

    updated_at: Optional[datetime] = FieldInfo(alias="updatedAt", default=None)
    """When the object schema was last updated."""

    updated_by_user_id: Optional[int] = FieldInfo(alias="updatedByUserId", default=None)
