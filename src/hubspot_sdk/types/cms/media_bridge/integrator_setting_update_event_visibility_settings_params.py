# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["IntegratorSettingUpdateEventVisibilitySettingsParams"]


class IntegratorSettingUpdateEventVisibilitySettingsParams(TypedDict, total=False):
    event_type: Required[
        Annotated[
            Literal["ALL", "MEDIA_PLAYS", "MEDIA_PLAYS_PERCENT", "ATTENTION_SPAN"], PropertyInfo(alias="eventType")
        ]
    ]

    updated_at: Required[Annotated[int, PropertyInfo(alias="updatedAt")]]

    show_in_reporting: Annotated[bool, PropertyInfo(alias="showInReporting")]

    show_in_timeline: Annotated[bool, PropertyInfo(alias="showInTimeline")]

    show_in_workflows: Annotated[bool, PropertyInfo(alias="showInWorkflows")]
