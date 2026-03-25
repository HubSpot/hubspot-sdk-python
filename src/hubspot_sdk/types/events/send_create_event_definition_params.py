# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo
from .external_behavioral_event_property_create_param import ExternalBehavioralEventPropertyCreateParam
from .external_object_resolution_mapping_request_param import ExternalObjectResolutionMappingRequestParam

__all__ = ["SendCreateEventDefinitionParams"]


class SendCreateEventDefinitionParams(TypedDict, total=False):
    include_default_properties: Required[Annotated[bool, PropertyInfo(alias="includeDefaultProperties")]]

    label: Required[str]
    """Human readable label for the event for display in HubSpot's UI."""

    property_definitions: Required[
        Annotated[Iterable[ExternalBehavioralEventPropertyCreateParam], PropertyInfo(alias="propertyDefinitions")]
    ]
    """List of custom properties on event"""

    custom_matching_id: Annotated[ExternalObjectResolutionMappingRequestParam, PropertyInfo(alias="customMatchingId")]

    description: str
    """A description of the event that will be shown as help text in HubSpot."""

    name: str
    """Internal event name, which must be used when referencing the event from the API.

    If a name is not supplied, one will be generated based on the label. The name
    does not include the `pe<PORTAL_ID>_` prefix used when sending event
    completions.
    """

    primary_object: Annotated[str, PropertyInfo(alias="primaryObject")]
    """The object type to associate this event to.

    Can be one of `CONTACT`, `COMPANY`, `DEAL`, `TICKET`. If no value is supplied,
    will default to `CONTACT`.
    """
