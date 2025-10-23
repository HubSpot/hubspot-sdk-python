# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["PublicSetOccurrencesRefineBy"]


class PublicSetOccurrencesRefineBy(BaseModel):
    set_type: str = FieldInfo(alias="setType")

    type: Literal["SET_OCCURRENCES"]
