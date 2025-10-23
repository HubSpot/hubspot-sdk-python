# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["APIFetchedObjectPropertyValue"]


class APIFetchedObjectPropertyValue(BaseModel):
    property_token: str = FieldInfo(alias="propertyToken")
    """The token to use to identify the object property to use"""

    type: Literal["FETCHED_OBJECT_PROPERTY"]
    """This is the type of input value.

    This can be one of: "FIELD_DATA", "OBJECT_PROPERTY", "STATIC_VALUE",
    "RELATIVE_DATETIME", "TIMESTAMP", "INCREMENT", "FETCHED_OBJECT_PROPERTY",
    "APPEND_OBJECT_PROPERTY", "STATIC_APPEND_VALUE", "ENROLLMENT_EVENT_PROPERTY"
    """
