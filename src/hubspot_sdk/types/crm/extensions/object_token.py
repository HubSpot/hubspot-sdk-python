# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["ObjectToken"]


class ObjectToken(BaseModel):
    value: str

    data_type: Optional[
        Literal["BOOLEAN", "CURRENCY", "DATE", "DATETIME", "EMAIL", "LINK", "NUMERIC", "STATUS", "STRING"]
    ] = FieldInfo(alias="dataType", default=None)

    label: Optional[str] = None

    name: Optional[str] = None
