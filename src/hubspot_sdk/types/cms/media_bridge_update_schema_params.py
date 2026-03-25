# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo
from ..shared_params.object_type_definition_labels import ObjectTypeDefinitionLabels

__all__ = ["MediaBridgeUpdateSchemaParams"]


class MediaBridgeUpdateSchemaParams(TypedDict, total=False):
    app_id: Required[Annotated[str, PropertyInfo(alias="appId")]]

    clear_description: Required[Annotated[bool, PropertyInfo(alias="clearDescription")]]

    allows_sensitive_properties: Annotated[bool, PropertyInfo(alias="allowsSensitiveProperties")]

    description: str

    labels: ObjectTypeDefinitionLabels

    primary_display_property: Annotated[str, PropertyInfo(alias="primaryDisplayProperty")]

    required_properties: Annotated[SequenceNotStr[str], PropertyInfo(alias="requiredProperties")]

    restorable: bool

    searchable_properties: Annotated[SequenceNotStr[str], PropertyInfo(alias="searchableProperties")]

    secondary_display_properties: Annotated[SequenceNotStr[str], PropertyInfo(alias="secondaryDisplayProperties")]
