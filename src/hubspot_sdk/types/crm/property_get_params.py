# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["PropertyGetParams"]


class PropertyGetParams(TypedDict, total=False):
    object_type: Required[Annotated[str, PropertyInfo(alias="objectType")]]

    archived: bool
    """Whether to return only results that have been archived."""

    data_sensitivity: Annotated[
        Literal["non_sensitive", "sensitive", "highly_sensitive"], PropertyInfo(alias="dataSensitivity")
    ]

    locale: str

    properties: str
