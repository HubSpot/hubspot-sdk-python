# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["IntegratorSettingGetEventVisibilitySettingsResponse", "VisibilitySetting"]


class VisibilitySetting(BaseModel):
    event_type: Literal["ALL", "MEDIA_PLAYS", "MEDIA_PLAYS_PERCENT", "ATTENTION_SPAN"] = FieldInfo(alias="eventType")

    updated_at: int = FieldInfo(alias="updatedAt")

    show_in_reporting: Optional[bool] = FieldInfo(alias="showInReporting", default=None)

    show_in_timeline: Optional[bool] = FieldInfo(alias="showInTimeline", default=None)

    show_in_workflows: Optional[bool] = FieldInfo(alias="showInWorkflows", default=None)


class IntegratorSettingGetEventVisibilitySettingsResponse(BaseModel):
    created_at: datetime = FieldInfo(alias="createdAt")

    visibility_settings: List[VisibilitySetting] = FieldInfo(alias="visibilitySettings")
