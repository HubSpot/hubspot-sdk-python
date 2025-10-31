# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["RecordingSettingsResponse"]


class RecordingSettingsResponse(BaseModel):
    url_to_retrieve_authed_recording: str = FieldInfo(alias="urlToRetrieveAuthedRecording")
    """The URL used to retrieve authenticated call recordings."""
