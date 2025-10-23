# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["APIAppendObjectPropertyValueParam"]


class APIAppendObjectPropertyValueParam(TypedDict, total=False):
    append_property_name: Required[Annotated[str, PropertyInfo(alias="appendPropertyName")]]
    """The name of the property to append data from"""

    type: Required[Literal["APPEND_OBJECT_PROPERTY"]]
    """This is the type of input value.

    This can be one of: "FIELD_DATA", "OBJECT_PROPERTY", "STATIC_VALUE",
    "RELATIVE_DATETIME", "TIMESTAMP", "INCREMENT", "FETCHED_OBJECT_PROPERTY",
    "APPEND_OBJECT_PROPERTY", "STATIC_APPEND_VALUE", "ENROLLMENT_EVENT_PROPERTY"
    """
