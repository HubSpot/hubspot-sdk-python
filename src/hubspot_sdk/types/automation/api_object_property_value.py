# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["APIObjectPropertyValue"]


class APIObjectPropertyValue(BaseModel):
    property_name: str = FieldInfo(alias="propertyName")

    type: Literal["OBJECT_PROPERTY"]
