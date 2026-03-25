# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import TYPE_CHECKING, Union
from typing_extensions import Literal, Required, TypeAlias, TypedDict, TypeAliasType

from ..._compat import PYDANTIC_V1
from .long_field_schema_param import LongFieldSchemaParam
from .double_field_schema_param import DoubleFieldSchemaParam
from .object_field_schema_param import ObjectFieldSchemaParam
from .string_field_schema_param import StringFieldSchemaParam
from .boolean_field_schema_param import BooleanFieldSchemaParam
from .integer_field_schema_param import IntegerFieldSchemaParam

__all__ = ["ArrayFieldSchemaParam", "Items"]

if TYPE_CHECKING or not PYDANTIC_V1:
    Items = TypeAliasType(
        "Items",
        Union[
            IntegerFieldSchemaParam,
            LongFieldSchemaParam,
            DoubleFieldSchemaParam,
            StringFieldSchemaParam,
            BooleanFieldSchemaParam,
            "ArrayFieldSchemaParam",
            ObjectFieldSchemaParam,
        ],
    )
else:
    Items: TypeAlias = Union[
        IntegerFieldSchemaParam,
        LongFieldSchemaParam,
        DoubleFieldSchemaParam,
        StringFieldSchemaParam,
        BooleanFieldSchemaParam,
        "ArrayFieldSchemaParam",
        ObjectFieldSchemaParam,
    ]


class ArrayFieldSchemaParam(TypedDict, total=False):
    items: Required[Items]

    type: Required[Literal["ARRAY"]]
