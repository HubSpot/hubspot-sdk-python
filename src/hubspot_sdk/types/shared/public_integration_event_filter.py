# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .public_event_filter_metadata import PublicEventFilterMetadata

__all__ = ["PublicIntegrationEventFilter"]


class PublicIntegrationEventFilter(BaseModel):
    event_type_id: int = FieldInfo(alias="eventTypeId")

    filter_lines: List[PublicEventFilterMetadata] = FieldInfo(alias="filterLines")

    filter_type: Literal["INTEGRATION_EVENT"] = FieldInfo(alias="filterType")
