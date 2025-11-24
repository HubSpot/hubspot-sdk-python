# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable
from typing_extensions import Required, Annotated, TypedDict

from ...._utils import PropertyInfo
from ..column_request_param import ColumnRequestParam

__all__ = ["TableUpdateDraftParams"]


class TableUpdateDraftParams(TypedDict, total=False):
    allow_child_tables: Required[Annotated[bool, PropertyInfo(alias="allowChildTables")]]
    """Specifies whether child tables can be created"""

    allow_public_api_access: Required[Annotated[bool, PropertyInfo(alias="allowPublicApiAccess")]]
    """Specifies whether the table can be read by public without authorization"""

    columns: Required[Iterable[ColumnRequestParam]]
    """List of columns in the table"""

    dynamic_meta_tags: Required[Annotated[Dict[str, int], PropertyInfo(alias="dynamicMetaTags")]]
    """
    Specifies the key value pairs of the
    [metadata fields](https://developers.hubspot.com/docs/cms/guides/dynamic-pages/hubdb#dynamic-pages)
    with the associated column IDs.
    """

    enable_child_table_pages: Required[Annotated[bool, PropertyInfo(alias="enableChildTablePages")]]
    """Specifies creation of multi-level dynamic pages using child tables"""

    label: Required[str]
    """Label of the table"""

    name: Required[str]
    """Name of the table"""

    use_for_pages: Required[Annotated[bool, PropertyInfo(alias="useForPages")]]
    """Specifies whether the table can be used for creation of dynamic pages"""

    archived: bool
    """Specifies whether to return archived tables. Defaults to `false`."""

    include_foreign_ids: Annotated[bool, PropertyInfo(alias="includeForeignIds")]
    """Set this to `true` to populate foreign ID values in the result."""

    is_get_localized_schema: Annotated[bool, PropertyInfo(alias="isGetLocalizedSchema")]
    """Indicates whether to retrieve the localized schema for the table."""
