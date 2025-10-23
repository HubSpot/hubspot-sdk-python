# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["LinkGenerationResponse"]


class LinkGenerationResponse(BaseModel):
    manage_preferences_url: str = FieldInfo(alias="managePreferencesUrl")

    subscriber_id_string: str = FieldInfo(alias="subscriberIdString")

    unsubscribe_all_url: str = FieldInfo(alias="unsubscribeAllUrl")

    unsubscribe_single_url: Optional[str] = FieldInfo(alias="unsubscribeSingleUrl", default=None)
