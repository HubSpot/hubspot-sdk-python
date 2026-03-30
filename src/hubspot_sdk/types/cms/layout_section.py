# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List

from pydantic import Field as FieldInfo

from .styles import Styles
from ..._models import BaseModel
from .row_meta_data import RowMetaData

__all__ = ["LayoutSection"]


class LayoutSection(BaseModel):
    cells: List["LayoutSection"]

    css_class: str = FieldInfo(alias="cssClass")
    """The CSS class applied to the layout section."""

    css_id: str = FieldInfo(alias="cssId")
    """The CSS ID applied to the layout section."""

    css_style: str = FieldInfo(alias="cssStyle")
    """Custom CSS styles applied to the layout section."""

    label: str
    """The label for the layout section."""

    name: str
    """The name assigned to the layout section."""

    params: Dict[str, object]
    """null"""

    row_meta_data: List[RowMetaData] = FieldInfo(alias="rowMetaData")

    rows: List[Dict[str, "LayoutSection"]]

    styles: Styles

    type: str
    """The type of the layout section."""

    w: int
    """The width of the layout section."""

    x: int
    """The x-coordinate position of the layout section."""
