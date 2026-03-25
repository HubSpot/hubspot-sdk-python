# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["PublicSetOccurrencesRefineByParam"]


class PublicSetOccurrencesRefineByParam(TypedDict, total=False):
    set_type: Required[Annotated[str, PropertyInfo(alias="setType")]]
    """
    Indicates the specific set type used in the refinement (ALL, ALL_INCLUDE_EMPTY,
    ANY, NONE, NONE_EXCLUDE_EMPTY, ANY_INCLUDE_EMPTY).
    """

    type: Required[Literal["SET_OCCURRENCES"]]
    """Specifies the type of refinement (SET_OCCURRENCES)."""
