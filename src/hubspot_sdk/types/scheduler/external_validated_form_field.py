# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["ExternalValidatedFormField"]


class ExternalValidatedFormField(BaseModel):
    is_custom: bool = FieldInfo(alias="isCustom")
    """Whether the form field is a custom field."""

    label: str
    """The text label associated with the form field."""

    name: str
    """
    The name identifier for the form field, includes underscores in place of spaces
    (e.g., the label `my form` is converted to `my_form`).
    """

    value: str
    """The value associated with the form field."""

    field_type: Optional[str] = FieldInfo(alias="fieldType", default=None)
    """The specific input type of the form field.

    Corresponds to property types (e.g., `select`, `radio`, `date`, etc).
    """

    translated_label: Optional[str] = FieldInfo(alias="translatedLabel", default=None)
    """The translated text label for the form field."""

    value_label: Optional[str] = FieldInfo(alias="valueLabel", default=None)
    """The text label associated to a form field selection or option."""
