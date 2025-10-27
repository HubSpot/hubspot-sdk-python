# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, Annotated, TypedDict

from ...._types import SequenceNotStr
from ...._utils import PropertyInfo
from .object_type_property_create_param import ObjectTypePropertyCreateParam
from ...shared_params.object_type_definition_labels import ObjectTypeDefinitionLabels

__all__ = ["SchemaCreateParams"]


class SchemaCreateParams(TypedDict, total=False):
    associated_objects: Required[Annotated[SequenceNotStr[str], PropertyInfo(alias="associatedObjects")]]
    """Associations defined for this object type."""

    labels: Required[ObjectTypeDefinitionLabels]

    name: Required[str]
    """A unique name for this object. For internal use only."""

    properties: Required[Iterable[ObjectTypePropertyCreateParam]]
    """Properties defined for this object type."""

    required_properties: Required[Annotated[SequenceNotStr[str], PropertyInfo(alias="requiredProperties")]]
    """
    The names of properties that should be **required** when creating an object of
    this type.
    """

    description: str

    primary_display_property: Annotated[str, PropertyInfo(alias="primaryDisplayProperty")]
    """The name of the primary property for this object.

    This will be displayed as primary on the HubSpot record page for this object
    type.
    """

    searchable_properties: Annotated[SequenceNotStr[str], PropertyInfo(alias="searchableProperties")]
    """
    Names of properties that will be indexed for this object type in by HubSpot's
    product search.
    """

    secondary_display_properties: Annotated[SequenceNotStr[str], PropertyInfo(alias="secondaryDisplayProperties")]
    """The names of secondary properties for this object.

    These will be displayed as secondary on the HubSpot record page for this object
    type.
    """
