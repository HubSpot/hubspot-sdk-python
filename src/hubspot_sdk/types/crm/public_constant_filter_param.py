# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["PublicConstantFilterParam"]


class PublicConstantFilterParam(TypedDict, total=False):
    filter_type: Required[Annotated[Literal["CONSTANT"], PropertyInfo(alias="filterType")]]
    """Specifies the type of filter, which is (CONSTANT)."""

    should_accept: Required[Annotated[bool, PropertyInfo(alias="shouldAccept")]]
    """Indicates whether the filter should accept the condition."""

    source: str
    """Defines the source of the constant filter."""
