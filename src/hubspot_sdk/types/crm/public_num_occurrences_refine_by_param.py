# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["PublicNumOccurrencesRefineByParam"]


class PublicNumOccurrencesRefineByParam(TypedDict, total=False):
    type: Required[Literal["NUM_OCCURRENCES"]]
    """The type of refinement (NUM_OCCURRENCES)."""

    max_occurrences: Annotated[int, PropertyInfo(alias="maxOccurrences")]
    """The maximum number of occurrences allowed."""

    min_occurrences: Annotated[int, PropertyInfo(alias="minOccurrences")]
    """The minimum number of occurrences required."""
