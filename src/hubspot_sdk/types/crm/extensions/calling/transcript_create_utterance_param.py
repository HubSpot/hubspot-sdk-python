# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ....._utils import PropertyInfo
from .speaker_param import SpeakerParam

__all__ = ["TranscriptCreateUtteranceParam"]


class TranscriptCreateUtteranceParam(TypedDict, total=False):
    end_time_millis: Required[Annotated[int, PropertyInfo(alias="endTimeMillis")]]

    speaker: Required[SpeakerParam]

    start_time_millis: Required[Annotated[int, PropertyInfo(alias="startTimeMillis")]]

    text: Required[str]

    language_code: Annotated[str, PropertyInfo(alias="languageCode")]
