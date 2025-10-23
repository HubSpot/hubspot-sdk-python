# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo
from .option_input_param import OptionInputParam

__all__ = ["PropertyCreateParam"]


class PropertyCreateParam(TypedDict, total=False):
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
    """Controls how the property appears in HubSpot."""

    group_name: Required[Annotated[str, PropertyInfo(alias="groupName")]]
    """The name of the property group the property belongs to."""

    label: Required[str]
    """A human-readable property label that will be shown in HubSpot."""

    name: Required[str]
    """
    The internal property name, which must be used when referencing the property via
    the API.
    """

    type: Required[Literal["bool", "date", "datetime", "enumeration", "number", "phone_number", "string"]]
    """The data type of the property."""

    calculation_formula: Annotated[str, PropertyInfo(alias="calculationFormula")]
    """Represents a formula that is used to compute a calculated property."""

    data_sensitivity: Annotated[
        Literal["non_sensitive", "sensitive", "highly_sensitive"], PropertyInfo(alias="dataSensitivity")
    ]

    description: str
    """A description of the property that will be shown as help text in HubSpot."""

    display_order: Annotated[int, PropertyInfo(alias="displayOrder")]
    """
    Properties are displayed in order starting with the lowest positive integer
    value. Values of -1 will cause the property to be displayed after any positive
    values.
    """

    external_options: Annotated[bool, PropertyInfo(alias="externalOptions")]
    """Applicable only for 'enumeration' type properties.

    Should be set to true in conjunction with a 'referencedObjectType' of 'OWNER'.
    Otherwise false.
    """

    form_field: Annotated[bool, PropertyInfo(alias="formField")]
    """Whether or not the property can be used in a HubSpot form."""

    has_unique_value: Annotated[bool, PropertyInfo(alias="hasUniqueValue")]
    """Whether or not the property's value must be unique.

    Once set, this can't be changed.
    """

    hidden: bool
    """
    If true, the option will not be shown in forms, bots, or meeting scheduling
    pages. Supported for contact, company, ticket, and custom object enumeration
    properties.
    """

    options: Iterable[OptionInputParam]
    """A list of valid options for the property.

    This field is required for enumerated properties.
    """

    referenced_object_type: Annotated[str, PropertyInfo(alias="referencedObjectType")]
    """
    Should be set to 'OWNER' when 'externalOptions' is true, which causes the
    property to dynamically pull option values from the current HubSpot users.
    """
