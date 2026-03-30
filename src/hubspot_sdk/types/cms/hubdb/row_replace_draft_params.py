# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Required, Annotated, TypedDict

from ...._utils import PropertyInfo
from ..variant_param import VariantParam

__all__ = ["RowReplaceDraftParams"]


class RowReplaceDraftParams(TypedDict, total=False):
    table_id_or_name: Required[Annotated[str, PropertyInfo(alias="tableIdOrName")]]

    child_table_id: Required[Annotated[int, PropertyInfo(alias="childTableId")]]
    """Specifies the value for the column child table id"""

    display_index: Required[Annotated[int, PropertyInfo(alias="displayIndex")]]
    """The index position for displaying the row within the table."""

    values: Required[Dict[str, VariantParam]]
    """List of key value pairs with the column name and column value"""

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
