# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["FileFieldParam"]


class FileFieldParam(TypedDict, total=False):
    """A form field used for uploading one or more files."""

    allow_multiple_files: Required[Annotated[bool, PropertyInfo(alias="allowMultipleFiles")]]
    """Whether to allow the upload of multiple files."""

    dependent_fields: Required[Annotated[Iterable["DependentFieldParam"], PropertyInfo(alias="dependentFields")]]
    """
    A list of other fields to make visible based on the value filled in for this
    field.
    """

    field_type: Required[Annotated[Literal["file"], PropertyInfo(alias="fieldType")]]
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

    required: Required[bool]
    """Whether a value for this field is required when submitting the form."""

    default_value: Annotated[str, PropertyInfo(alias="defaultValue")]
    """The value filled in by default.

    This value will be submitted unless the customer modifies it.
    """

    description: str
    """Additional text helping the customer to complete the field."""

    placeholder: str
    """The prompt text showing when the field isn't filled in."""


from .dependent_field_param import DependentFieldParam
