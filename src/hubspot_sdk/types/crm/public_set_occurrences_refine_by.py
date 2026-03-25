# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["PublicSetOccurrencesRefineBy"]


class PublicSetOccurrencesRefineBy(BaseModel):
    set_type: str = FieldInfo(alias="setType")
    """
    Indicates the specific set type used in the refinement (ALL, ALL_INCLUDE_EMPTY,
    ANY, NONE, NONE_EXCLUDE_EMPTY, ANY_INCLUDE_EMPTY).
    """

    type: Literal["SET_OCCURRENCES"]
    """Specifies the type of refinement (SET_OCCURRENCES)."""
