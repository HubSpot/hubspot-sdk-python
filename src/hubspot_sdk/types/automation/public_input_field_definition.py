# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .public_field_type_definition import PublicFieldTypeDefinition

__all__ = ["PublicInputFieldDefinition"]


class PublicInputFieldDefinition(BaseModel):
    is_required: bool = FieldInfo(alias="isRequired")

    type_definition: PublicFieldTypeDefinition = FieldInfo(alias="typeDefinition")

    supported_value_types: Optional[List[Literal["STATIC_VALUE", "OBJECT_PROPERTY"]]] = FieldInfo(
        alias="supportedValueTypes", default=None
    )
