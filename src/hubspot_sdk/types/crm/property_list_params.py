# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["PropertyListParams"]


class PropertyListParams(TypedDict, total=False):
    archived: bool
    """Whether to return only results that have been archived."""

    data_sensitivity: Annotated[
        Literal["non_sensitive", "sensitive", "highly_sensitive"], PropertyInfo(alias="dataSensitivity")
    ]

    locale: str

    properties: str
