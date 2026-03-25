# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo
from .public_option_param import PublicOptionParam

__all__ = ["PublicFieldTypeDefinitionParam"]


class PublicFieldTypeDefinitionParam(TypedDict, total=False):
    name: Required[str]

    options: Required[Iterable[PublicOptionParam]]

    type: Required[
        Literal[
            "bool", "date", "datetime", "enumeration", "json", "number", "object_coordinates", "phone_number", "string"
        ]
    ]

    description: str

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

    help_text: Annotated[str, PropertyInfo(alias="helpText")]

    label: str

    options_url: Annotated[str, PropertyInfo(alias="optionsUrl")]

    referenced_object_type: Annotated[Literal["OWNER"], PropertyInfo(alias="referencedObjectType")]
