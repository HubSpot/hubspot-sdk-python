# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .phone_field_validation import PhoneFieldValidation

__all__ = ["MobilePhoneField"]


class MobilePhoneField(BaseModel):
    """A form field used for collecting a mobile phone number."""

    dependent_fields: List["DependentField"] = FieldInfo(alias="dependentFields")
    """
    A list of other fields to make visible based on the value filled in for this
    field.
    """

    field_type: Literal["mobile_phone"] = FieldInfo(alias="fieldType")
    """Determines how the field will be displayed and validated."""

    hidden: bool
    """Whether a field should be hidden or not.

    Hidden fields won't appear on the form, but can be used to pass a value to a
    property without requiring the customer to fill it in.
    """

    label: str
    """The main label for the form field."""

    name: str
    """The identifier of the field.

    In combination with the object type ID, it must be unique.
    """

    object_type_id: str = FieldInfo(alias="objectTypeId")
    """A unique ID for this field's CRM object type.

    For example a CONTACT field will have the object type ID 0-1.
    """

    required: bool
    """Whether a value for this field is required when submitting the form."""

    validation: PhoneFieldValidation
    """Describes how a phone number should be validated."""

    default_value: Optional[str] = FieldInfo(alias="defaultValue", default=None)
    """The value filled in by default.

    This value will be submitted unless the customer modifies it.
    """

    description: Optional[str] = None
    """Additional text helping the customer to complete the field."""

    placeholder: Optional[str] = None
    """The prompt text showing when the field isn't filled in."""


from .dependent_field import DependentField
