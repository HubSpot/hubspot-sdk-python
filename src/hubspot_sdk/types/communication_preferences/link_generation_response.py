# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["LinkGenerationResponse"]


class LinkGenerationResponse(BaseModel):
    manage_preferences_url: str = FieldInfo(alias="managePreferencesUrl")
    """The URL where the subscriber can manage their communication preferences."""

    subscriber_id_string: str = FieldInfo(alias="subscriberIdString")
    """A string representing the unique identifier of the subscriber."""

    unsubscribe_all_url: str = FieldInfo(alias="unsubscribeAllUrl")
    """
    A string containing the URL for unsubscribing the subscriber from all
    communications.
    """

    unsubscribe_single_url: Optional[str] = FieldInfo(alias="unsubscribeSingleUrl", default=None)
    """
    A string containing the URL to unsubscribe the subscriber from a single
    communication.
    """
