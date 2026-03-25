# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .public_option import PublicOption

__all__ = ["PublicFieldTypeDefinition"]


class PublicFieldTypeDefinition(BaseModel):
    name: str

    options: List[PublicOption]

    type: Literal[
        "bool", "date", "datetime", "enumeration", "json", "number", "object_coordinates", "phone_number", "string"
    ]

    description: Optional[str] = None

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

    help_text: Optional[str] = FieldInfo(alias="helpText", default=None)

    label: Optional[str] = None

    options_url: Optional[str] = FieldInfo(alias="optionsUrl", default=None)

    referenced_object_type: Optional[Literal["OWNER"]] = FieldInfo(alias="referencedObjectType", default=None)
