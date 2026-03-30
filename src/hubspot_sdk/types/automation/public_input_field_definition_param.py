# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo
from .public_field_type_definition_param import PublicFieldTypeDefinitionParam

__all__ = ["PublicInputFieldDefinitionParam"]


class PublicInputFieldDefinitionParam(TypedDict, total=False):
    is_required: Required[Annotated[bool, PropertyInfo(alias="isRequired")]]
    """Indicates whether the input field is mandatory."""

    type_definition: Required[Annotated[PublicFieldTypeDefinitionParam, PropertyInfo(alias="typeDefinition")]]

    supported_value_types: Annotated[
        List[Literal["STATIC_VALUE", "OBJECT_PROPERTY"]], PropertyInfo(alias="supportedValueTypes")
    ]
