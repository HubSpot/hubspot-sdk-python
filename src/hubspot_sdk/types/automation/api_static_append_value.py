# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["APIStaticAppendValue"]


class APIStaticAppendValue(BaseModel):
    static_append_value: str = FieldInfo(alias="staticAppendValue")

    type: Literal["STATIC_APPEND_VALUE"]
