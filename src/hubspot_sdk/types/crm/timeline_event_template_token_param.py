# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo
from .timeline_event_template_token_option_param import TimelineEventTemplateTokenOptionParam

__all__ = ["TimelineEventTemplateTokenParam"]


class TimelineEventTemplateTokenParam(TypedDict, total=False):
    label: Required[str]
    """Used for list segmentation and reporting."""

    name: Required[str]
    """The name of the token referenced in the templates.

    This must be unique for the specific template. It may only contain alphanumeric
    characters, periods, dashes, or underscores (. - \\__).
    """

    type: Required[Literal["date", "enumeration", "number", "string"]]
    """The data type of the token.

    You can currently choose from [string, number, date, enumeration].
    """

    created_at: Annotated[Union[str, datetime], PropertyInfo(alias="createdAt", format="iso8601")]
    """
    The date and time that the Event Template Token was created, as an ISO 8601
    timestamp. Will be null if the template was created before Feb 18th, 2020.
    """

    object_property_name: Annotated[str, PropertyInfo(alias="objectPropertyName")]
    """The name of the CRM object property.

    This will populate the CRM object property associated with the event. With
    enough of these, you can fully build CRM objects via the Timeline API.
    """

    options: Iterable[TimelineEventTemplateTokenOptionParam]
    """If type is `enumeration`, we should have a list of options to choose from."""

    updated_at: Annotated[Union[str, datetime], PropertyInfo(alias="updatedAt", format="iso8601")]
    """
    The date and time that the Event Template Token was last updated, as an ISO 8601
    timestamp. Will be null if the template was created before Feb 18th, 2020.
    """
