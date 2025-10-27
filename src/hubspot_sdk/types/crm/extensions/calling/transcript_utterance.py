# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .speaker import Speaker
from ....._models import BaseModel

__all__ = ["TranscriptUtterance"]


class TranscriptUtterance(BaseModel):
    id: str

    end_time_millis: int = FieldInfo(alias="endTimeMillis")

    start_time_millis: int = FieldInfo(alias="startTimeMillis")

    text: str

    language_code: Optional[str] = FieldInfo(alias="languageCode", default=None)

    speaker: Optional[Speaker] = None
