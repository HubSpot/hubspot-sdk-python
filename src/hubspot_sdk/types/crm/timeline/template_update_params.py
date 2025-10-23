# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, Annotated, TypedDict

from ...._utils import PropertyInfo
from ..timeline_event_template_token_param import TimelineEventTemplateTokenParam

__all__ = ["TemplateUpdateParams"]


class TemplateUpdateParams(TypedDict, total=False):
    app_id: Required[Annotated[int, PropertyInfo(alias="appId")]]

    id: Required[str]
    """The template ID."""

    name: Required[str]
    """The template name."""

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
