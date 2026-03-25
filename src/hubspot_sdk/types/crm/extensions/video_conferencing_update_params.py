# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["VideoConferencingUpdateParams"]


class VideoConferencingUpdateParams(TypedDict, total=False):
    create_meeting_url: Required[Annotated[str, PropertyInfo(alias="createMeetingUrl")]]

    delete_meeting_url: Annotated[str, PropertyInfo(alias="deleteMeetingUrl")]

    fetch_accounts_uri: Annotated[str, PropertyInfo(alias="fetchAccountsUri")]

    update_meeting_url: Annotated[str, PropertyInfo(alias="updateMeetingUrl")]

    user_verify_url: Annotated[str, PropertyInfo(alias="userVerifyUrl")]
