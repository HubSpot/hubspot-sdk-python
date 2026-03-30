# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["TableGetParams"]


class TableGetParams(TypedDict, total=False):
    archived: bool
    """Whether to return only results that have been archived."""

    include_foreign_ids: Annotated[bool, PropertyInfo(alias="includeForeignIds")]

    is_get_localized_schema: Annotated[bool, PropertyInfo(alias="isGetLocalizedSchema")]
