# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .external_option import ExternalOption

__all__ = ["ExternalLinkFormField"]


class ExternalLinkFormField(BaseModel):
    field_type: str = FieldInfo(alias="fieldType")

    is_custom: bool = FieldInfo(alias="isCustom")

    is_required: bool = FieldInfo(alias="isRequired")

    label: str

    name: str

    options: List[ExternalOption]

    type: str
