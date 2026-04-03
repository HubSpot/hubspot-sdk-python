# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["SettingCreateOrUpdateParams"]


class SettingCreateOrUpdateParams(TypedDict, total=False):
    event_details_url: Required[Annotated[str, PropertyInfo(alias="eventDetailsUrl")]]
    """The url that will be used to fetch marketing event details by id.

    Must contain a `%s` character sequence that will be substituted with the event
    id. For example: `https://my.event.app/events/%s`
    """
