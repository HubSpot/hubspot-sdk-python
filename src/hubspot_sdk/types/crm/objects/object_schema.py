# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ..property import Property
from ...._models import BaseModel
from .association_definition import AssociationDefinition
from .object_type_definition_labels import ObjectTypeDefinitionLabels

__all__ = ["ObjectSchema"]


class ObjectSchema(BaseModel):
    id: str
    """A unique ID for this schema's object type.

    Will be defined as {meta-type}-{unique ID}.
    """

    associations: List[AssociationDefinition]
    """Associations defined for a given object type."""

    labels: ObjectTypeDefinitionLabels
    """Singular and plural labels for the object. Used in CRM display."""

    name: str
    """A unique name for the schema's object type."""

    properties: List[Property]
    """Properties defined for this object type."""

    required_properties: List[str] = FieldInfo(alias="requiredProperties")
    """
    The names of properties that should be **required** when creating an object of
    this type.
    """

    archived: Optional[bool] = None

    created_at: Optional[datetime] = FieldInfo(alias="createdAt", default=None)
    """When the object schema was created."""

    created_by_user_id: Optional[int] = FieldInfo(alias="createdByUserId", default=None)

    description: Optional[str] = None

    fully_qualified_name: Optional[str] = FieldInfo(alias="fullyQualifiedName", default=None)
    """An assigned unique ID for the object, including portal ID and object name."""

    object_type_id: Optional[str] = FieldInfo(alias="objectTypeId", default=None)

    primary_display_property: Optional[str] = FieldInfo(alias="primaryDisplayProperty", default=None)
    """The name of the primary property for this object.

    This will be displayed as primary on the HubSpot record page for this object
    type.
    """

    searchable_properties: Optional[List[str]] = FieldInfo(alias="searchableProperties", default=None)
    """
    Names of properties that will be indexed for this object type in by HubSpot's
    product search.
    """

    secondary_display_properties: Optional[List[str]] = FieldInfo(alias="secondaryDisplayProperties", default=None)
    """The names of secondary properties for this object.

    These will be displayed as secondary on the HubSpot record page for this object
    type.
    """

    updated_at: Optional[datetime] = FieldInfo(alias="updatedAt", default=None)
    """When the object schema was last updated."""

    updated_by_user_id: Optional[int] = FieldInfo(alias="updatedByUserId", default=None)
