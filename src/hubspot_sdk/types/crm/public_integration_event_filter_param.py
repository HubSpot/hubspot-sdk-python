# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo
from .public_event_filter_metadata_param import PublicEventFilterMetadataParam

__all__ = ["PublicIntegrationEventFilterParam"]


class PublicIntegrationEventFilterParam(TypedDict, total=False):
    event_type_id: Required[Annotated[int, PropertyInfo(alias="eventTypeId")]]
    """The ID representing the type of event for the integration event filter."""

    filter_lines: Required[Annotated[Iterable[PublicEventFilterMetadataParam], PropertyInfo(alias="filterLines")]]

    filter_type: Required[Annotated[Literal["INTEGRATION_EVENT"], PropertyInfo(alias="filterType")]]
    """Indicates the type of filter (INTEGRATION_EVENT)."""
