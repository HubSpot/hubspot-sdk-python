# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .external_option import ExternalOption

__all__ = ["ExternalLinkFormField"]


class ExternalLinkFormField(BaseModel):
    field_type: str = FieldInfo(alias="fieldType")
    """The specific field type of the form field.

    Corresponds to property types (e.g., `select`, `radio`, `date`, etc)
    """

    is_custom: bool = FieldInfo(alias="isCustom")
    """Whether the form field is a custom field."""

    is_required: bool = FieldInfo(alias="isRequired")
    """Whether the form field is mandatory."""

    label: str
    """The text label for the form field."""

    name: str
    """The name identifier for the form field."""

    options: List[ExternalOption]

    type: str
    """The data type of the form field accepts (e.g. `date`, `enumeration`, etc)"""
