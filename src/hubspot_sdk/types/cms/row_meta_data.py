# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import Field as FieldInfo

from .styles import Styles
from ..._models import BaseModel

__all__ = ["RowMetaData"]


class RowMetaData(BaseModel):
    css_class: str = FieldInfo(alias="cssClass")

    styles: Styles
