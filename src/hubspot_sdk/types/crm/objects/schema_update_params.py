# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ...._types import SequenceNotStr
from ...._utils import PropertyInfo
from ...shared_params.object_type_definition_labels import ObjectTypeDefinitionLabels

__all__ = ["SchemaUpdateParams"]


class SchemaUpdateParams(TypedDict, total=False):
    clear_description: Annotated[bool, PropertyInfo(alias="clearDescription")]

    description: str

    labels: ObjectTypeDefinitionLabels

    primary_display_property: Annotated[str, PropertyInfo(alias="primaryDisplayProperty")]
    """The name of the primary property for this object.

    This will be displayed as primary on the HubSpot record page for this object
    type.
    """

    required_properties: Annotated[SequenceNotStr[str], PropertyInfo(alias="requiredProperties")]
    """
    The names of properties that should be **required** when creating an object of
    this type.
    """

    restorable: bool

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
