# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["PublicOptionParam"]


class PublicOptionParam(TypedDict, total=False):
    label: Required[str]

    value: Required[str]

    description: str

    display_order: Annotated[int, PropertyInfo(alias="displayOrder")]
