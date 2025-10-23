# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["PublicConstantFilter"]


class PublicConstantFilter(TypedDict, total=False):
    filter_type: Required[Annotated[Literal["CONSTANT"], PropertyInfo(alias="filterType")]]

    should_accept: Required[Annotated[bool, PropertyInfo(alias="shouldAccept")]]

    source: str
