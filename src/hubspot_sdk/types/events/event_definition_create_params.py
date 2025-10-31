# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo
from ..shared_params.option_input import OptionInput

__all__ = ["EventDefinitionCreateParams", "PropertyDefinition"]


class EventDefinitionCreateParams(TypedDict, total=False):
    label: Required[str]
    """Human readable label for the event. Used in HubSpot UI"""

    property_definitions: Required[Annotated[Iterable[PropertyDefinition], PropertyInfo(alias="propertyDefinitions")]]
    """List of custom properties on event"""

    description: str
    """A description of the event that will be shown as help text in HubSpot."""

    name: str
    """
    Internal event name, which must be used when referencing the event from this
    event definitions API. If a name is not supplied, one will be generated based on
    the label. The `name` value will also be used to automatically generate a
    `fullyQualifiedName` for the event definition, which you'll use when sending
    event completions to this event.
    """

    primary_object: Annotated[str, PropertyInfo(alias="primaryObject")]
    """The object type to associate this event to.

    Can be one of CONTACT, COMPANY, DEAL, TICKET. If no primaryObject is supplied,
    we will default to associating the event to CONTACT objects.
    """


class PropertyDefinition(TypedDict, total=False):
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
