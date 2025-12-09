# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .enumerated_field_option import EnumeratedFieldOption

__all__ = ["RadioField"]


class RadioField(BaseModel):
    """
    A form field consisting of a set of radio options, out of which one can be selected at a time.
    """

    default_values: List[str] = FieldInfo(alias="defaultValues")
    """The values selected by default.

    Those values will be submitted unless the customer modifies them.
    """

    dependent_fields: List["DependentField"] = FieldInfo(alias="dependentFields")
    """
    A list of other fields to make visible based on the value filled in for this
    field.
    """

    field_type: Literal["radio"] = FieldInfo(alias="fieldType")
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

    options: List[EnumeratedFieldOption]
    """The list of available choices for this field."""

    required: bool
    """Whether a value for this field is required when submitting the form."""

    description: Optional[str] = None
    """Additional text helping the customer to complete the field."""

    placeholder: Optional[str] = None
    """The prompt text showing when the field isn't filled in."""


from .dependent_field import DependentField
