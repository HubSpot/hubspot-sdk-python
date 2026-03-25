# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["EventDetailSettings"]


class EventDetailSettings(BaseModel):
    app_id: int = FieldInfo(alias="appId")
    """The id of the application the settings are for"""

    event_details_url: str = FieldInfo(alias="eventDetailsUrl")
    """The url that will be used to fetch marketing event details by id"""
