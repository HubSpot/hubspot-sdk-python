# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, Annotated, TypedDict

from ...._utils import PropertyInfo
from ..timeline_event_template_token_param import TimelineEventTemplateTokenParam

__all__ = ["TemplateCreateParams"]


class TemplateCreateParams(TypedDict, total=False):
    name: Required[str]
    """The template name."""

    object_type: Required[Annotated[str, PropertyInfo(alias="objectType")]]
    """The type of CRM object this template is for.

    [Contacts, companies, tickets, and deals] are supported.
    """

    tokens: Required[Iterable[TimelineEventTemplateTokenParam]]
    """
    A collection of tokens that can be used as custom properties on the event and to
    create fully fledged CRM objects.
    """

    detail_template: Annotated[str, PropertyInfo(alias="detailTemplate")]
    """
    This uses Markdown syntax with Handlebars and event-specific data to render HTML
    on a timeline when you expand the details.
    """

    header_template: Annotated[str, PropertyInfo(alias="headerTemplate")]
    """
    This uses Markdown syntax with Handlebars and event-specific data to render HTML
    on a timeline as a header.
    """
