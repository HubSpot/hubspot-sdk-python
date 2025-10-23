# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["SetOccurrencesRefineBy"]


class SetOccurrencesRefineBy(BaseModel):
    set_type: Literal["ALL", "ALL_INCLUDE_EMPTY", "ANY", "NONE", "NONE_EXCLUDE_EMPTY", "ANY_INCLUDE_EMPTY"] = FieldInfo(
        alias="setType"
    )

    type: Literal["SetOccurrencesRefineBy"]
