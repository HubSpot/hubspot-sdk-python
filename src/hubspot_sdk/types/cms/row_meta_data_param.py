# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo
from .styles_param import StylesParam

__all__ = ["RowMetaDataParam"]


class RowMetaDataParam(TypedDict, total=False):
    css_class: Required[Annotated[str, PropertyInfo(alias="cssClass")]]

    styles: Required[StylesParam]
