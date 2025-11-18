# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from .column import Column
from ..._models import BaseModel
from .simple_user import SimpleUser

__all__ = ["HubDBTableV3"]


class HubDBTableV3(BaseModel):
    id: str
    """Id of the table"""

    allow_child_tables: bool = FieldInfo(alias="allowChildTables")
    """Specifies whether child tables can be created"""

    allow_public_api_access: bool = FieldInfo(alias="allowPublicApiAccess")
    """Specifies whether the table can be read by public without authorization"""

    column_count: int = FieldInfo(alias="columnCount")
    """Number of columns including deleted"""

    columns: List[Column]
    """List of columns in the table"""

    created_at: datetime = FieldInfo(alias="createdAt")
    """Timestamp at which the table is created"""

    deleted: bool

    deleted_at: datetime = FieldInfo(alias="deletedAt")

    dynamic_meta_tags: Dict[str, int] = FieldInfo(alias="dynamicMetaTags")
    """
    Specifies the key value pairs of the
    [metadata fields](https://developers.hubspot.com/docs/cms/guides/dynamic-pages/hubdb#dynamic-pages)
    with the associated column IDs.
    """

    enable_child_table_pages: bool = FieldInfo(alias="enableChildTablePages")
    """Specifies creation of multi-level dynamic pages using child tables"""

    label: str
    """Label of the table"""

    name: str
    """Name of the table"""

    published: bool

    published_at: datetime = FieldInfo(alias="publishedAt")
    """Timestamp at which the table is published recently"""

    row_count: int = FieldInfo(alias="rowCount")
    """Number of rows in the table"""

    updated_at: datetime = FieldInfo(alias="updatedAt")
    """Timestamp at which the table is updated recently"""

    use_for_pages: bool = FieldInfo(alias="useForPages")
    """Specifies whether the table can be used for creation of dynamic pages"""

    created_by: Optional[SimpleUser] = FieldInfo(alias="createdBy", default=None)

    is_ordered_manually: Optional[bool] = FieldInfo(alias="isOrderedManually", default=None)

    updated_by: Optional[SimpleUser] = FieldInfo(alias="updatedBy", default=None)
