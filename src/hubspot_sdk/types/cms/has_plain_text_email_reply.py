# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["HasPlainTextEmailReply"]


class HasPlainTextEmailReply(BaseModel):
    operator: Literal["HAS_PLAIN_TEXT_EMAIL_REPLY"]

    inputs: Optional[List["Expression"]] = None

    property_name: Optional[str] = FieldInfo(alias="propertyName", default=None)

    value: Optional[bool] = None


from .expression import Expression
