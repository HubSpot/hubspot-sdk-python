# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

from ..shared_params.option_input import OptionInput

__all__ = ["EventDefinitionCreatePropertyParams"]


class EventDefinitionCreatePropertyParams(TypedDict, total=False):
    label: Required[str]
    """Human readable label for the property. Used in HubSpot UI"""

    type: Required[str]
    """The data type of the property.

    Can be one of the following: [string, number, enumeration, datetime]
    """

    description: str
    """A description of the property that will be shown as help text in HubSpot."""

    name: str
    """
    Internal property name, which must be used when referencing the property from
    the API
    """

    options: Iterable[OptionInput]
    """A list of available options for the property if it is an enumeration.

    NOTE: This field is only applicable for enumerated properties.
    """
