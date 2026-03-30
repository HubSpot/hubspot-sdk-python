# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .public_option import PublicOption

__all__ = ["PublicFieldTypeDefinition"]


class PublicFieldTypeDefinition(BaseModel):
    name: str
    """The internal name used to identify the field."""

    options: List[PublicOption]

    type: Literal[
        "bool", "date", "datetime", "enumeration", "json", "number", "object_coordinates", "phone_number", "string"
    ]
    """
    The data type of the field, with accepted values including bool, date, datetime,
    enumeration, json, number, object_coordinates, phone_number, and string.
    """

    description: Optional[str] = None
    """A detailed explanation of the field's purpose."""

    field_type: Optional[
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
        ]
    ] = FieldInfo(alias="fieldType", default=None)
    """
    The type of field, with accepted values including booleancheckbox,
    calculation_equation, checkbox, date, file, html, number, phonenumber, radio,
    select, text, and textarea.
    """

    help_text: Optional[str] = FieldInfo(alias="helpText", default=None)
    """Additional information or guidance about the field."""

    label: Optional[str] = None
    """A user-friendly name for the field."""

    options_url: Optional[str] = FieldInfo(alias="optionsUrl", default=None)
    """A URL that provides options for the field."""

    referenced_object_type: Optional[Literal["OWNER"]] = FieldInfo(alias="referencedObjectType", default=None)
    """
    The type of object that the field references, with accepted values including
    OWNER.
    """
