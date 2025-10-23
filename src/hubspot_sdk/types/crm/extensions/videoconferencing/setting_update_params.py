# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ....._utils import PropertyInfo

__all__ = ["SettingUpdateParams"]


class SettingUpdateParams(TypedDict, total=False):
    create_meeting_url: Required[Annotated[str, PropertyInfo(alias="createMeetingUrl")]]
    """The URL that HubSpot will send requests to create a new video conference."""

    delete_meeting_url: Annotated[str, PropertyInfo(alias="deleteMeetingUrl")]
    """
    The URL that HubSpot will send notifications of meetings that have been deleted
    in HubSpot.
    """

    fetch_accounts_uri: Annotated[str, PropertyInfo(alias="fetchAccountsUri")]

    update_meeting_url: Annotated[str, PropertyInfo(alias="updateMeetingUrl")]
    """The URL that HubSpot will send updates to existing meetings.

    Typically called when the user changes the topic or times of a meeting.
    """

    user_verify_url: Annotated[str, PropertyInfo(alias="userVerifyUrl")]
    """
    The URL that HubSpot will use to verify that a user exists in the video
    conference application.
    """
