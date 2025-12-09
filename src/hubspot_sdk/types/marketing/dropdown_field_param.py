# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo
from .enumerated_field_option_param import EnumeratedFieldOptionParam

__all__ = ["DropdownFieldParam"]


class DropdownFieldParam(TypedDict, total=False):
    """A field consisting of a drop down with multiple choices."""

    default_values: Required[Annotated[SequenceNotStr[str], PropertyInfo(alias="defaultValues")]]
    """The values selected by default.

    Those values will be submitted unless the customer modifies them.
    """

    dependent_fields: Required[Annotated[Iterable["DependentFieldParam"], PropertyInfo(alias="dependentFields")]]
    """
    A list of other fields to make visible based on the value filled in for this
    field.
    """

    field_type: Required[Annotated[Literal["dropdown"], PropertyInfo(alias="fieldType")]]
    """Determines how the field will be displayed and validated."""

    hidden: Required[bool]
    """Whether a field should be hidden or not.

    Hidden fields won't appear on the form, but can be used to pass a value to a
    property without requiring the customer to fill it in.
    """

    label: Required[str]
    """The main label for the form field."""

    name: Required[str]
    """The identifier of the field.

    In combination with the object type ID, it must be unique.
    """

    object_type_id: Required[Annotated[str, PropertyInfo(alias="objectTypeId")]]
    """A unique ID for this field's CRM object type.

    For example a CONTACT field will have the object type ID 0-1.
    """

    options: Required[Iterable[EnumeratedFieldOptionParam]]
    """The list of available choices for this field."""

    required: Required[bool]
    """Whether a value for this field is required when submitting the form."""

    description: str
    """Additional text helping the customer to complete the field."""

    placeholder: str
    """The prompt text showing when the field isn't filled in."""


from .dependent_field_param import DependentFieldParam
