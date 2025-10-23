# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["PublicMigrationMapping"]


class PublicMigrationMapping(BaseModel):
    legacy_list_id: str = FieldInfo(alias="legacyListId")
    """The legacy list id for the list"""

    list_id: str = FieldInfo(alias="listId")
    """The V3 list id for the list"""
