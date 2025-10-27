# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from datetime import datetime

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .event_visibility_change import EventVisibilityChange

__all__ = ["EventVisibilityResponse"]


class EventVisibilityResponse(BaseModel):
    created_at: datetime = FieldInfo(alias="createdAt")

    visibility_settings: List[EventVisibilityChange] = FieldInfo(alias="visibilitySettings")
