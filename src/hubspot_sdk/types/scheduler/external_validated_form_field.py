# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["ExternalValidatedFormField"]


class ExternalValidatedFormField(BaseModel):
    is_custom: bool = FieldInfo(alias="isCustom")

    label: str

    name: str

    value: str

    field_type: Optional[str] = FieldInfo(alias="fieldType", default=None)

    translated_label: Optional[str] = FieldInfo(alias="translatedLabel", default=None)

    value_label: Optional[str] = FieldInfo(alias="valueLabel", default=None)
