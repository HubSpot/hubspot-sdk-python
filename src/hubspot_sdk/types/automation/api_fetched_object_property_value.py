# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["APIFetchedObjectPropertyValue"]


class APIFetchedObjectPropertyValue(BaseModel):
    property_token: str = FieldInfo(alias="propertyToken")

    type: Literal["FETCHED_OBJECT_PROPERTY"]
