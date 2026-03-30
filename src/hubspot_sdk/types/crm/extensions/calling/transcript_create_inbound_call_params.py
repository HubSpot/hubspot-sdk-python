# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from ....._utils import PropertyInfo
from ..formatted_phone_number_param import FormattedPhoneNumberParam

__all__ = ["TranscriptCreateInboundCallParams"]


class TranscriptCreateInboundCallParams(TypedDict, total=False):
    create_engagement: Required[Annotated[bool, PropertyInfo(alias="createEngagement")]]
    """Indicates whether an engagement should be created for the call."""

    engagement_properties: Required[Annotated[Dict[str, str], PropertyInfo(alias="engagementProperties")]]
    """Contains additional properties related to the engagement."""

    external_call_id: Required[Annotated[str, PropertyInfo(alias="externalCallId")]]
    """The unique identifier for the call from an external system."""

    final_call_status: Required[
        Annotated[
            Literal[
                "BUSY",
                "CALLING_CRM_USER",
                "CANCELED",
                "COMPLETED",
                "CONNECTING",
                "FAILED",
                "HOLD",
                "IN_PROGRESS",
                "MISSED",
                "NO_ANSWER",
                "QUEUED",
                "RINGING",
                "UNKNOWN",
            ],
            PropertyInfo(alias="finalCallStatus"),
        ]
    ]
    """
    The final status of the call, with accepted values including: BUSY,
    CALLING_CRM_USER, CANCELED, COMPLETED, CONNECTING, FAILED, HOLD, IN_PROGRESS,
    MISSED, NO_ANSWER, QUEUED, RINGING, UNKNOWN.
    """

    from_number: Required[Annotated[FormattedPhoneNumberParam, PropertyInfo(alias="fromNumber")]]

    potential_recipient_user_ids: Required[Annotated[Iterable[int], PropertyInfo(alias="potentialRecipientUserIds")]]

    to_number: Required[Annotated[FormattedPhoneNumberParam, PropertyInfo(alias="toNumber")]]

    call_started_timestamp: Annotated[
        Union[str, datetime], PropertyInfo(alias="callStartedTimestamp", format="iso8601")
    ]
    """
    The timestamp indicating when the call started, formatted as a date-time string.
    """

    duration_seconds: Annotated[int, PropertyInfo(alias="durationSeconds")]
    """The duration of the call in seconds."""

    user_id: Annotated[int, PropertyInfo(alias="userId")]
    """The ID of the user associated with the call."""
