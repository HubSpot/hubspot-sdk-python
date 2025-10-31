# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["NumOccurrencesRefineBy"]


class NumOccurrencesRefineBy(BaseModel):
    type: Literal["NumOccurrencesRefineBy"]

    max_occurrences: Optional[int] = FieldInfo(alias="maxOccurrences", default=None)

    min_occurrences: Optional[int] = FieldInfo(alias="minOccurrences", default=None)
