# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["PublicConstantFilter"]


class PublicConstantFilter(BaseModel):
    filter_type: Literal["CONSTANT"] = FieldInfo(alias="filterType")

    should_accept: bool = FieldInfo(alias="shouldAccept")

    source: Optional[str] = None
