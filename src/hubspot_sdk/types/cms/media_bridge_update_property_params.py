# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo
from ..shared_params.option_input import OptionInput

__all__ = ["MediaBridgeUpdatePropertyParams"]


class MediaBridgeUpdatePropertyParams(TypedDict, total=False):
    app_id: Required[Annotated[str, PropertyInfo(alias="appId")]]

    object_type: Required[Annotated[str, PropertyInfo(alias="objectType")]]

    calculation_formula: Annotated[str, PropertyInfo(alias="calculationFormula")]

    description: str

    display_order: Annotated[int, PropertyInfo(alias="displayOrder")]

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

    form_field: Annotated[bool, PropertyInfo(alias="formField")]

    group_name: Annotated[str, PropertyInfo(alias="groupName")]

    has_unique_value: Annotated[bool, PropertyInfo(alias="hasUniqueValue")]

    hidden: bool

    label: str

    options: Iterable[OptionInput]

    type: Literal["bool", "date", "datetime", "enumeration", "number", "phone_number", "string"]
