# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .timeline_event_template_token_option import TimelineEventTemplateTokenOption

__all__ = ["TimelineEventTemplateToken"]


class TimelineEventTemplateToken(BaseModel):
    label: str
    """Used for list segmentation and reporting."""

    name: str
    """The name of the token referenced in the templates.

    This must be unique for the specific template. It may only contain alphanumeric
    characters, periods, dashes, or underscores (. - \\__).
    """

    type: Literal["date", "enumeration", "number", "string"]
    """The data type of the token.

    You can currently choose from [string, number, date, enumeration].
    """

    created_at: Optional[datetime] = FieldInfo(alias="createdAt", default=None)
    """
    The date and time that the Event Template Token was created, as an ISO 8601
    timestamp. Will be null if the template was created before Feb 18th, 2020.
    """

    object_property_name: Optional[str] = FieldInfo(alias="objectPropertyName", default=None)
    """The name of the CRM object property.

    This will populate the CRM object property associated with the event. With
    enough of these, you can fully build CRM objects via the Timeline API.
    """

    options: Optional[List[TimelineEventTemplateTokenOption]] = None
    """If type is `enumeration`, we should have a list of options to choose from."""

    updated_at: Optional[datetime] = FieldInfo(alias="updatedAt", default=None)
    """
    The date and time that the Event Template Token was last updated, as an ISO 8601
    timestamp. Will be null if the template was created before Feb 18th, 2020.
    """
