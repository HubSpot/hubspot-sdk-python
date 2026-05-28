# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo
from .option_input import OptionInput

__all__ = ["PropertyCreate"]


class PropertyCreate(TypedDict, total=False):
    field_type: Required[
        Annotated[
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
    ]

    group_name: Required[Annotated[str, PropertyInfo(alias="groupName")]]

    label: Required[str]

    name: Required[str]

    type: Required[Literal["bool", "date", "datetime", "enumeration", "number", "phone_number", "string"]]

    calculation_formula: Annotated[str, PropertyInfo(alias="calculationFormula")]

    currency_property_name: Annotated[str, PropertyInfo(alias="currencyPropertyName")]

    data_sensitivity: Annotated[
        Literal["highly_sensitive", "non_sensitive", "sensitive"], PropertyInfo(alias="dataSensitivity")
    ]

    description: str

    display_order: Annotated[int, PropertyInfo(alias="displayOrder")]

    external_options: Annotated[bool, PropertyInfo(alias="externalOptions")]

    form_field: Annotated[bool, PropertyInfo(alias="formField")]

    has_unique_value: Annotated[bool, PropertyInfo(alias="hasUniqueValue")]

    hidden: bool

    number_display_hint: Annotated[
        Literal["currency", "duration", "formatted", "percentage", "probability", "unformatted"],
        PropertyInfo(alias="numberDisplayHint"),
    ]

    options: Iterable[OptionInput]

    referenced_object_type: Annotated[str, PropertyInfo(alias="referencedObjectType")]

    show_currency_symbol: Annotated[bool, PropertyInfo(alias="showCurrencySymbol")]

    text_display_hint: Annotated[
        Literal[
            "domain_name",
            "email",
            "ip_address",
            "multi_line",
            "phone_number",
            "physical_address",
            "postal_code",
            "unformatted_single_line",
        ],
        PropertyInfo(alias="textDisplayHint"),
    ]
