# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo
from ..shared_params.option_input import OptionInput

__all__ = ["PropertyUpdateParams"]


class PropertyUpdateParams(TypedDict, total=False):
    object_type: Required[Annotated[str, PropertyInfo(alias="objectType")]]

    calculation_formula: Annotated[str, PropertyInfo(alias="calculationFormula")]
    """Represents a formula that is used to compute a calculated property."""

    currency_property_name: Annotated[str, PropertyInfo(alias="currencyPropertyName")]

    description: str
    """A description of the property that will be shown as help text in HubSpot."""

    display_order: Annotated[int, PropertyInfo(alias="displayOrder")]
    """
    Properties are displayed in order starting with the lowest positive integer
    value. Values of -1 will cause the Property to be displayed after any positive
    values.
    """

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
    """Controls how the property appears in HubSpot."""

    form_field: Annotated[bool, PropertyInfo(alias="formField")]
    """Whether or not the property can be used in a HubSpot form."""

    group_name: Annotated[str, PropertyInfo(alias="groupName")]
    """The name of the property group the property belongs to."""

    hidden: bool
    """If true, the property won't be visible and can't be used in HubSpot."""

    label: str
    """A human-readable property label that will be shown in HubSpot."""

    number_display_hint: Annotated[
        Literal["currency", "duration", "formatted", "percentage", "probability", "unformatted"],
        PropertyInfo(alias="numberDisplayHint"),
    ]

    options: Iterable[OptionInput]
    """A list of valid options for the property."""

    show_currency_symbol: Annotated[bool, PropertyInfo(alias="showCurrencySymbol")]

    type: Literal["bool", "date", "datetime", "enumeration", "number", "phone_number", "string"]
    """The data type of the property."""
