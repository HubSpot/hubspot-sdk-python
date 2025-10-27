# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, Annotated, TypedDict

from ....._utils import PropertyInfo
from .transcript_create_utterance_param import TranscriptCreateUtteranceParam

__all__ = ["TranscriptCreateParams"]


class TranscriptCreateParams(TypedDict, total=False):
    engagement_id: Required[Annotated[int, PropertyInfo(alias="engagementId")]]

    transcript_create_utterances: Required[
        Annotated[Iterable[TranscriptCreateUtteranceParam], PropertyInfo(alias="transcriptCreateUtterances")]
    ]
