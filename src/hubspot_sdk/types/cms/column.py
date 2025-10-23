# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .foreign_id import ForeignID
from .simple_user import SimpleUser
from ..shared.option import Option

__all__ = ["Column"]


class Column(BaseModel):
    label: str
    """Label of the column"""

    name: str
    """Name of the column"""

    type: Literal[
        "NULL",
        "TEXT",
        "NUMBER",
        "URL",
        "IMAGE",
        "SELECT",
        "MULTISELECT",
        "BOOLEAN",
        "LOCATION",
        "DATE",
        "DATETIME",
        "CURRENCY",
        "RICHTEXT",
        "FOREIGN_ID",
        "VIDEO",
        "CTA",
        "FILE",
        "JSON",
        "COMPOSITE",
        "CODE",
        "HUBSPOT_VIDEO",
        "EMBED",
    ]
    """Type of the column"""

    id: Optional[str] = None
    """Column Id"""

    created_at: Optional[datetime] = FieldInfo(alias="createdAt", default=None)

    created_by: Optional[SimpleUser] = FieldInfo(alias="createdBy", default=None)

    created_by_user_id: Optional[int] = FieldInfo(alias="createdByUserId", default=None)

    deleted: Optional[bool] = None

    description: Optional[str] = None

    foreign_column_id: Optional[int] = FieldInfo(alias="foreignColumnId", default=None)
    """Foreign Column id"""

    foreign_ids: Optional[List[ForeignID]] = FieldInfo(alias="foreignIds", default=None)
    """Foreign Ids"""

    foreign_ids_by_id: Optional[Dict[str, ForeignID]] = FieldInfo(alias="foreignIdsById", default=None)
    """Foreign ids"""

    foreign_ids_by_name: Optional[Dict[str, ForeignID]] = FieldInfo(alias="foreignIdsByName", default=None)
    """Foreign ids by name"""

    foreign_table_id: Optional[int] = FieldInfo(alias="foreignTableId", default=None)
    """Foreign table id referenced"""

    option_count: Optional[int] = FieldInfo(alias="optionCount", default=None)
    """Number of options available"""

    options: Optional[List[Option]] = None
    """Options to choose for select and multi-select columns"""

    updated_at: Optional[datetime] = FieldInfo(alias="updatedAt", default=None)

    updated_by: Optional[SimpleUser] = FieldInfo(alias="updatedBy", default=None)

    updated_by_user_id: Optional[int] = FieldInfo(alias="updatedByUserId", default=None)

    width: Optional[int] = None
    """Column width for HubDB UI"""
