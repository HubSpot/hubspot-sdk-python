# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["QuickReply"]


class QuickReply(BaseModel):
    value: str

    value_type: Literal["TEXT", "URL"] = FieldInfo(alias="valueType")

    label: Optional[str] = None
