# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["ExternalSettings"]


class ExternalSettings(BaseModel):
    create_meeting_url: str = FieldInfo(alias="createMeetingUrl")

    delete_meeting_url: Optional[str] = FieldInfo(alias="deleteMeetingUrl", default=None)

    fetch_accounts_uri: Optional[str] = FieldInfo(alias="fetchAccountsUri", default=None)

    update_meeting_url: Optional[str] = FieldInfo(alias="updateMeetingUrl", default=None)

    user_verify_url: Optional[str] = FieldInfo(alias="userVerifyUrl", default=None)
