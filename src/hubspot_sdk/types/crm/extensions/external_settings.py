# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["ExternalSettings"]


class ExternalSettings(BaseModel):
    """The URLs of the various actions provided by the video conferencing application.

    All URLs must use the `https` protocol.
    """

    create_meeting_url: str = FieldInfo(alias="createMeetingUrl")
    """The URL that HubSpot will send requests to create a new video conference."""

    delete_meeting_url: Optional[str] = FieldInfo(alias="deleteMeetingUrl", default=None)
    """
    The URL that HubSpot will send notifications of meetings that have been deleted
    in HubSpot.
    """

    fetch_accounts_uri: Optional[str] = FieldInfo(alias="fetchAccountsUri", default=None)

    update_meeting_url: Optional[str] = FieldInfo(alias="updateMeetingUrl", default=None)
    """The URL that HubSpot will send updates to existing meetings.

    Typically called when the user changes the topic or times of a meeting.
    """

    user_verify_url: Optional[str] = FieldInfo(alias="userVerifyUrl", default=None)
    """
    The URL that HubSpot will use to verify that a user exists in the video
    conference application.
    """
