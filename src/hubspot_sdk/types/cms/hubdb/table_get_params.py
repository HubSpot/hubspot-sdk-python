# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["TableGetParams"]


class TableGetParams(TypedDict, total=False):
    archived: bool
    """Set this to `true` to return details for an archived table.

    Defaults to `false`.
    """

    include_foreign_ids: Annotated[bool, PropertyInfo(alias="includeForeignIds")]
    """Set this to `true` to populate foreign ID values in the result."""

    is_get_localized_schema: Annotated[bool, PropertyInfo(alias="isGetLocalizedSchema")]
    """Indicates whether to retrieve the localized schema for the tables."""
