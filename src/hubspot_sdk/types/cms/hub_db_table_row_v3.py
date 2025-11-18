# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict
from datetime import datetime

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["HubDBTableRowV3"]


class HubDBTableRowV3(BaseModel):
    id: str
    """The id of the table row"""

    child_table_id: str = FieldInfo(alias="childTableId")
    """Specifies the value for the column child table id"""

    created_at: datetime = FieldInfo(alias="createdAt")
    """Timestamp at which the row is created"""

    name: str
    """
    Specifies the value for `hs_name` column, which will be used as title in the
    dynamic pages
    """

    path: str
    """
    Specifies the value for `hs_path` column, which will be used as slug in the
    dynamic pages
    """

    published_at: datetime = FieldInfo(alias="publishedAt")

    updated_at: datetime = FieldInfo(alias="updatedAt")
    """Timestamp at which the row is updated last time"""

    values: Dict[str, object]
    """List of key value pairs with the column name and column value"""
