# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo
from .public_event_filter_metadata import PublicEventFilterMetadata

__all__ = ["PublicIntegrationEventFilter"]


class PublicIntegrationEventFilter(TypedDict, total=False):
    event_type_id: Required[Annotated[int, PropertyInfo(alias="eventTypeId")]]

    filter_lines: Required[Annotated[Iterable[PublicEventFilterMetadata], PropertyInfo(alias="filterLines")]]

    filter_type: Required[Annotated[Literal["INTEGRATION_EVENT"], PropertyInfo(alias="filterType")]]
