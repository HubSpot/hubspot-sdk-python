# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .timeline_event_i_frame import TimelineEventIFrame

__all__ = ["AppEventOccurrence"]


class AppEventOccurrence(BaseModel):
    id: str

    event_type_name: str = FieldInfo(alias="eventTypeName")

    properties: Dict[str, str]

    domain: Optional[str] = None

    email: Optional[str] = None

    extra_data: Optional[object] = FieldInfo(alias="extraData", default=None)

    object_id: Optional[str] = FieldInfo(alias="objectId", default=None)

    object_type_fully_qualified_name: Optional[str] = FieldInfo(alias="objectTypeFullyQualifiedName", default=None)

    timeline_i_frame: Optional[TimelineEventIFrame] = FieldInfo(alias="timelineIFrame", default=None)

    timestamp: Optional[datetime] = None

    utk: Optional[str] = None
