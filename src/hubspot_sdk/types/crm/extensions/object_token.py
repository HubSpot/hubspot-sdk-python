# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["ObjectToken"]


class ObjectToken(BaseModel):
    value: str
    """The value of the property"""

    data_type: Optional[
        Literal["BOOLEAN", "CURRENCY", "DATE", "DATETIME", "EMAIL", "LINK", "NUMERIC", "STATUS", "STRING"]
    ] = FieldInfo(alias="dataType", default=None)
    """The type of the property.

    Can be one of CURRENCY, DATE, DATETIME, EMAIL, LINK, NUMERIC, STATUS
    """

    label: Optional[str] = None
    """The label of the property as it will be displayed to users"""

    name: Optional[str] = None
    """The name of the property"""
