# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["EventVisibilityChange"]


class EventVisibilityChange(BaseModel):
    event_type: Literal["ALL", "ATTENTION_SPAN", "MEDIA_PLAYS", "MEDIA_PLAYS_PERCENT"] = FieldInfo(alias="eventType")

    updated_at: int = FieldInfo(alias="updatedAt")

    show_in_reporting: Optional[bool] = FieldInfo(alias="showInReporting", default=None)

    show_in_timeline: Optional[bool] = FieldInfo(alias="showInTimeline", default=None)

    show_in_workflows: Optional[bool] = FieldInfo(alias="showInWorkflows", default=None)
