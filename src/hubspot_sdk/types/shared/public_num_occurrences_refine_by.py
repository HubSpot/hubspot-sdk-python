# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["PublicNumOccurrencesRefineBy"]


class PublicNumOccurrencesRefineBy(BaseModel):
    type: Literal["NUM_OCCURRENCES"]

    max_occurrences: Optional[int] = FieldInfo(alias="maxOccurrences", default=None)

    min_occurrences: Optional[int] = FieldInfo(alias="minOccurrences", default=None)
