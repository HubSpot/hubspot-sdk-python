# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo
from .option_input_param import OptionInputParam

__all__ = ["SendUpdateEventDefinitionPropertyParams"]


class SendUpdateEventDefinitionPropertyParams(TypedDict, total=False):
    event_name: Required[Annotated[str, PropertyInfo(alias="eventName")]]

    description: str
    """A description of the property that will be shown as help text in HubSpot."""

    label: str
    """Human readable label for the property. Used in HubSpot UI"""

    options: Iterable[OptionInputParam]
    """A list of available options for the property if it is an enumeration.

    NOTE: This field is only applicable for enumerated properties.
    """
