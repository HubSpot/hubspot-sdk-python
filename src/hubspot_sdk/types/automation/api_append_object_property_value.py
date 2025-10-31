# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["APIAppendObjectPropertyValue"]


class APIAppendObjectPropertyValue(BaseModel):
    append_property_name: str = FieldInfo(alias="appendPropertyName")

    type: Literal["APPEND_OBJECT_PROPERTY"]
