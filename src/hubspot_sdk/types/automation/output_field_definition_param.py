# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo
from .field_type_definition_param import FieldTypeDefinitionParam

__all__ = ["OutputFieldDefinitionParam"]


class OutputFieldDefinitionParam(TypedDict, total=False):
    type_definition: Required[Annotated[FieldTypeDefinitionParam, PropertyInfo(alias="typeDefinition")]]
