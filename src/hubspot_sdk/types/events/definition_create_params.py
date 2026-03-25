# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo
from .external_behavioral_event_property_create_param import ExternalBehavioralEventPropertyCreateParam
from .external_object_resolution_mapping_request_param import ExternalObjectResolutionMappingRequestParam

__all__ = ["DefinitionCreateParams"]


class DefinitionCreateParams(TypedDict, total=False):
    include_default_properties: Required[Annotated[bool, PropertyInfo(alias="includeDefaultProperties")]]

    label: Required[str]
    """Human readable label for the event. Used in HubSpot UI"""

    property_definitions: Required[
        Annotated[Iterable[ExternalBehavioralEventPropertyCreateParam], PropertyInfo(alias="propertyDefinitions")]
    ]
    """List of custom properties on event"""

    custom_matching_id: Annotated[ExternalObjectResolutionMappingRequestParam, PropertyInfo(alias="customMatchingId")]

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
