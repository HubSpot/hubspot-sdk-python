# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable
from typing_extensions import Required, Annotated, TypedDict

from ...._utils import PropertyInfo
from .styles_param import StylesParam
from .row_meta_data_param import RowMetaDataParam

__all__ = ["LayoutSectionParam"]


class LayoutSectionParam(TypedDict, total=False):
    cells: Required[Iterable["LayoutSectionParam"]]

    css_class: Required[Annotated[str, PropertyInfo(alias="cssClass")]]
    """The CSS class applied to the layout section."""

    css_id: Required[Annotated[str, PropertyInfo(alias="cssId")]]
    """The CSS ID applied to the layout section."""

    css_style: Required[Annotated[str, PropertyInfo(alias="cssStyle")]]
    """Custom CSS styles applied to the layout section."""

    label: Required[str]
    """The label for the layout section."""

    name: Required[str]
    """The name assigned to the layout section."""

    params: Required[Dict[str, object]]
    """Parameters associated with the layout section."""

    row_meta_data: Required[Annotated[Iterable[RowMetaDataParam], PropertyInfo(alias="rowMetaData")]]

    rows: Required[Iterable[Dict[str, "LayoutSectionParam"]]]

    styles: Required[StylesParam]

    type: Required[str]
    """The type of the layout section."""

    w: Required[int]
    """The width of the layout section."""

    x: Required[int]
    """The x-coordinate position of the layout section."""
