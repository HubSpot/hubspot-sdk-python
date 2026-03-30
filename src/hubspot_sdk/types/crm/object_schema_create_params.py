# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo
from .object_type_property_create_param import ObjectTypePropertyCreateParam
from ..shared_params.object_type_definition_labels import ObjectTypeDefinitionLabels

__all__ = ["ObjectSchemaCreateParams"]


class ObjectSchemaCreateParams(TypedDict, total=False):
    allows_sensitive_properties: Required[Annotated[bool, PropertyInfo(alias="allowsSensitiveProperties")]]
    """
    Determines if the object type can include properties that are marked as
    sensitive.
    """

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

    searchable_properties: Required[Annotated[SequenceNotStr[str], PropertyInfo(alias="searchableProperties")]]
    """
    Names of properties that will be indexed for this object type in by HubSpot's
    product search.
    """

    secondary_display_properties: Required[
        Annotated[SequenceNotStr[str], PropertyInfo(alias="secondaryDisplayProperties")]
    ]
    """The names of secondary properties for this object.

    These will be displayed as secondary on the HubSpot record page for this object
    type.
    """

    description: str
    """A brief explanation of the object type."""

    primary_display_property: Annotated[str, PropertyInfo(alias="primaryDisplayProperty")]
    """The name of the primary property for this object.

    This will be displayed as primary on the HubSpot record page for this object
    type.
    """
