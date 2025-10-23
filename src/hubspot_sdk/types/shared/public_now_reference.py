# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["PublicNowReference"]


class PublicNowReference(BaseModel):
    reference_type: Literal["NOW"] = FieldInfo(alias="referenceType")

    hour: Optional[int] = None

    millisecond: Optional[int] = None

    minute: Optional[int] = None

    second: Optional[int] = None
