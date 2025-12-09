# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .timeline_event_template_token import TimelineEventTemplateToken

__all__ = ["TimelineEventTemplate"]


class TimelineEventTemplate(BaseModel):
    """The current state of the template definition."""

    id: str
    """The template ID."""

    name: str
    """The template name."""

    object_type: str = FieldInfo(alias="objectType")
    """The type of CRM object this template is for.

    [Contacts, companies, tickets, and deals] are supported.
    """

    tokens: List[TimelineEventTemplateToken]
    """
    A collection of tokens that can be used as custom properties on the event and to
    create fully fledged CRM objects.
    """

    created_at: Optional[datetime] = FieldInfo(alias="createdAt", default=None)
    """The date and time that the Event Template was created, as an ISO 8601 timestamp.

    Will be null if the template was created before Feb 18th, 2020.
    """

    detail_template: Optional[str] = FieldInfo(alias="detailTemplate", default=None)
    """
    This uses Markdown syntax with Handlebars and event-specific data to render HTML
    on a timeline when you expand the details.
    """

    header_template: Optional[str] = FieldInfo(alias="headerTemplate", default=None)
    """
    This uses Markdown syntax with Handlebars and event-specific data to render HTML
    on a timeline as a header.
    """

    updated_at: Optional[datetime] = FieldInfo(alias="updatedAt", default=None)
    """
    The date and time that the Event Template was last updated, as an ISO 8601
    timestamp. Will be null if the template was created before Feb 18th, 2020.
    """
