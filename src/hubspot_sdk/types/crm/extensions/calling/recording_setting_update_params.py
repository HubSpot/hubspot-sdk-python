# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ....._utils import PropertyInfo

__all__ = ["RecordingSettingUpdateParams"]


class RecordingSettingUpdateParams(TypedDict, total=False):
    url_to_retrieve_authed_recording: Annotated[str, PropertyInfo(alias="urlToRetrieveAuthedRecording")]
