# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ....._models import BaseModel
from .transcript_utterance import TranscriptUtterance

__all__ = ["TranscriptResponse"]


class TranscriptResponse(BaseModel):
    id: str

    created_at: datetime = FieldInfo(alias="createdAt")

    engagement_id: int = FieldInfo(alias="engagementId")

    transcript_source: Literal["HUBSPOT_GENERATED", "INTEGRATOR_GENERATED"] = FieldInfo(alias="transcriptSource")

    transcript_utterances: List[TranscriptUtterance] = FieldInfo(alias="transcriptUtterances")

    updated_at: datetime = FieldInfo(alias="updatedAt")
