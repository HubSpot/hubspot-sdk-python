# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["QuickReply"]


class QuickReply(BaseModel):
    value: str

    value_type: str = FieldInfo(alias="valueType")

    label: Optional[str] = None
