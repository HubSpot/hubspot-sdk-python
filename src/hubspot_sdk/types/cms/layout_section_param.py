# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo
from .styles_param import StylesParam
from .row_meta_data_param import RowMetaDataParam

__all__ = ["LayoutSectionParam"]


class LayoutSectionParam(TypedDict, total=False):
    cells: Required[Iterable["LayoutSectionParam"]]

    css_class: Required[Annotated[str, PropertyInfo(alias="cssClass")]]

    css_id: Required[Annotated[str, PropertyInfo(alias="cssId")]]

    css_style: Required[Annotated[str, PropertyInfo(alias="cssStyle")]]

    label: Required[str]

    name: Required[str]

    params: Required[Dict[str, object]]
    """null"""

    row_meta_data: Required[Annotated[Iterable[RowMetaDataParam], PropertyInfo(alias="rowMetaData")]]

    rows: Required[Iterable[Dict[str, "LayoutSectionParam"]]]

    styles: Required[StylesParam]

    type: Required[str]

    w: Required[int]

    x: Required[int]
