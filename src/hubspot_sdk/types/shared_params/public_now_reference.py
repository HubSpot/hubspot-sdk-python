# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["PublicNowReference"]


class PublicNowReference(TypedDict, total=False):
    reference_type: Required[Annotated[Literal["NOW"], PropertyInfo(alias="referenceType")]]

    hour: int

    millisecond: int

    minute: int

    second: int
