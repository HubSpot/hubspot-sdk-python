# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import TYPE_CHECKING, Union
from typing_extensions import Literal, TypeAlias, TypeAliasType

from ..._compat import PYDANTIC_V1
from ..._models import BaseModel
from .long_field_schema import LongFieldSchema
from .double_field_schema import DoubleFieldSchema
from .object_field_schema import ObjectFieldSchema
from .string_field_schema import StringFieldSchema
from .boolean_field_schema import BooleanFieldSchema
from .integer_field_schema import IntegerFieldSchema

__all__ = ["ArrayFieldSchema", "Items"]

if TYPE_CHECKING or not PYDANTIC_V1:
    Items = TypeAliasType(
        "Items",
        Union[
            IntegerFieldSchema,
            LongFieldSchema,
            DoubleFieldSchema,
            StringFieldSchema,
            BooleanFieldSchema,
            "ArrayFieldSchema",
            ObjectFieldSchema,
        ],
    )
else:
    Items: TypeAlias = Union[
        IntegerFieldSchema,
        LongFieldSchema,
        DoubleFieldSchema,
        StringFieldSchema,
        BooleanFieldSchema,
        "ArrayFieldSchema",
        ObjectFieldSchema,
    ]


class ArrayFieldSchema(BaseModel):
    items: Items

    type: Literal["ARRAY"]
