# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["ExternalOption"]


class ExternalOption(BaseModel):
    description: str

    display_order: int = FieldInfo(alias="displayOrder")

    double_data: float = FieldInfo(alias="doubleData")

    hidden: bool

    label: str

    read_only: bool = FieldInfo(alias="readOnly")

    value: str
