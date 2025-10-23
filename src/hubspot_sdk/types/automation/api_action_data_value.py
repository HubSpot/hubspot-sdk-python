# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["APIActionDataValue"]


class APIActionDataValue(BaseModel):
    action_id: str = FieldInfo(alias="actionId")
    """Which action to pull data from."""

    data_key: str = FieldInfo(alias="dataKey")
    """The output field name for that action"""

    type: Literal["FIELD_DATA"]
    """This is the type of input value.

    This can be one of: "FIELD_DATA", "OBJECT_PROPERTY", "STATIC_VALUE",
    "RELATIVE_DATETIME", "TIMESTAMP", "INCREMENT", "FETCHED_OBJECT_PROPERTY",
    "APPEND_OBJECT_PROPERTY", "STATIC_APPEND_VALUE", "ENROLLMENT_EVENT_PROPERTY"
    """
