# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union
from datetime import datetime
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo
from .timeline_event_i_frame_param import TimelineEventIFrameParam

__all__ = ["TimelineCreateEventParams"]


class TimelineCreateEventParams(TypedDict, total=False):
    id: Required[str]

    event_type_name: Required[Annotated[str, PropertyInfo(alias="eventTypeName")]]

    properties: Required[Dict[str, str]]

    domain: str

    email: str

    extra_data: Annotated[object, PropertyInfo(alias="extraData")]

    object_id: Annotated[str, PropertyInfo(alias="objectId")]

    object_type_fully_qualified_name: Annotated[str, PropertyInfo(alias="objectTypeFullyQualifiedName")]

    timeline_i_frame: Annotated[TimelineEventIFrameParam, PropertyInfo(alias="timelineIFrame")]

    timestamp: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]

    utk: str
