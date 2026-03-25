# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .object_type_definition_labels import ObjectTypeDefinitionLabels

__all__ = ["ObjectTypeDefinitionPatch"]


class ObjectTypeDefinitionPatch(BaseModel):
    clear_description: bool = FieldInfo(alias="clearDescription")

    allows_sensitive_properties: Optional[bool] = FieldInfo(alias="allowsSensitiveProperties", default=None)

    description: Optional[str] = None

    labels: Optional[ObjectTypeDefinitionLabels] = None

    primary_display_property: Optional[str] = FieldInfo(alias="primaryDisplayProperty", default=None)

    required_properties: Optional[List[str]] = FieldInfo(alias="requiredProperties", default=None)

    restorable: Optional[bool] = None

    searchable_properties: Optional[List[str]] = FieldInfo(alias="searchableProperties", default=None)

    secondary_display_properties: Optional[List[str]] = FieldInfo(alias="secondaryDisplayProperties", default=None)
