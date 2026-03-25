# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["OwnerGetParams"]


class OwnerGetParams(TypedDict, total=False):
    archived: bool
    """Whether to return only results that have been archived."""

    id_property: Annotated[Literal["id", "userId"], PropertyInfo(alias="idProperty")]
