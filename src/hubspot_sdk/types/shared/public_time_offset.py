# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["PublicTimeOffset"]


class PublicTimeOffset(BaseModel):
    amount: int

    offset_direction: str = FieldInfo(alias="offsetDirection")

    time_unit: str = FieldInfo(alias="timeUnit")
