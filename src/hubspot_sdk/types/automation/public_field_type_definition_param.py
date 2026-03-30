# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo
from .public_option_param import PublicOptionParam

__all__ = ["PublicFieldTypeDefinitionParam"]


class PublicFieldTypeDefinitionParam(TypedDict, total=False):
    name: Required[str]
    """The internal name used to identify the field."""

    options: Required[Iterable[PublicOptionParam]]

    type: Required[
        Literal[
            "bool", "date", "datetime", "enumeration", "json", "number", "object_coordinates", "phone_number", "string"
        ]
    ]
    """
    The data type of the field, with accepted values including bool, date, datetime,
    enumeration, json, number, object_coordinates, phone_number, and string.
    """

    description: str
    """A detailed explanation of the field's purpose."""

    field_type: Annotated[
        Literal[
            "booleancheckbox",
            "calculation_equation",
            "checkbox",
            "date",
            "file",
            "html",
            "number",
            "phonenumber",
            "radio",
            "select",
            "text",
            "textarea",
        ],
        PropertyInfo(alias="fieldType"),
    ]
    """
    The type of field, with accepted values including booleancheckbox,
    calculation_equation, checkbox, date, file, html, number, phonenumber, radio,
    select, text, and textarea.
    """

    help_text: Annotated[str, PropertyInfo(alias="helpText")]
    """Additional information or guidance about the field."""

    label: str
    """A user-friendly name for the field."""

    options_url: Annotated[str, PropertyInfo(alias="optionsUrl")]
    """A URL that provides options for the field."""

    referenced_object_type: Annotated[Literal["OWNER"], PropertyInfo(alias="referencedObjectType")]
    """
    The type of object that the field references, with accepted values including
    OWNER.
    """
