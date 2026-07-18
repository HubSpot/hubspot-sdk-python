# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .option_input import OptionInput

__all__ = ["PropertyCreate"]


class PropertyCreate(BaseModel):
    field_type: Literal[
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
    ] = FieldInfo(alias="fieldType")

    group_name: str = FieldInfo(alias="groupName")

    label: str

    name: str

    type: Literal["bool", "date", "datetime", "enumeration", "number", "phone_number", "string"]

    calculation_formula: Optional[str] = FieldInfo(alias="calculationFormula", default=None)

    currency_property_name: Optional[str] = FieldInfo(alias="currencyPropertyName", default=None)

    data_sensitivity: Optional[Literal["highly_sensitive", "non_sensitive", "sensitive"]] = FieldInfo(
        alias="dataSensitivity", default=None
    )

    description: Optional[str] = None

    display_order: Optional[int] = FieldInfo(alias="displayOrder", default=None)

    external_options: Optional[bool] = FieldInfo(alias="externalOptions", default=None)

    form_field: Optional[bool] = FieldInfo(alias="formField", default=None)

    has_unique_value: Optional[bool] = FieldInfo(alias="hasUniqueValue", default=None)

    hidden: Optional[bool] = None

    number_display_hint: Optional[
        Literal["currency", "duration", "formatted", "percentage", "probability", "unformatted"]
    ] = FieldInfo(alias="numberDisplayHint", default=None)

    options: Optional[List[OptionInput]] = None

    referenced_object_type: Optional[str] = FieldInfo(alias="referencedObjectType", default=None)

    show_currency_symbol: Optional[bool] = FieldInfo(alias="showCurrencySymbol", default=None)

    text_display_hint: Optional[
        Literal[
            "domain_name",
            "email",
            "ip_address",
            "multi_line",
            "phone_number",
            "physical_address",
            "postal_code",
            "unformatted_single_line",
        ]
    ] = FieldInfo(alias="textDisplayHint", default=None)
