# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, Annotated, TypedDict

from ...._utils import PropertyInfo
from ..timeline_event_template_token_option_param import TimelineEventTemplateTokenOptionParam

__all__ = ["TokenUpdateParams"]


class TokenUpdateParams(TypedDict, total=False):
    app_id: Required[Annotated[int, PropertyInfo(alias="appId")]]

    event_template_id: Required[Annotated[str, PropertyInfo(alias="eventTemplateId")]]

    label: Required[str]
    """Used for list segmentation and reporting."""

    object_property_name: Annotated[str, PropertyInfo(alias="objectPropertyName")]
    """The name of the CRM object property.

    This will populate the CRM object property associated with the event. With
    enough of these, you can fully build CRM objects via the Timeline API.
    """

    options: Iterable[TimelineEventTemplateTokenOptionParam]
    """If type is `enumeration`, we should have a list of options to choose from."""
