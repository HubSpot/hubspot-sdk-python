# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["PublicNumOccurrencesRefineBy"]


class PublicNumOccurrencesRefineBy(TypedDict, total=False):
    type: Required[Literal["NUM_OCCURRENCES"]]

    max_occurrences: Annotated[int, PropertyInfo(alias="maxOccurrences")]

    min_occurrences: Annotated[int, PropertyInfo(alias="minOccurrences")]
