# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["CallingCreateRecordingSettingsParams"]


class CallingCreateRecordingSettingsParams(TypedDict, total=False):
    url_to_retrieve_authed_recording: Required[Annotated[str, PropertyInfo(alias="urlToRetrieveAuthedRecording")]]
    """The URL used to access authenticated call recordings."""
