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

    engagement_properties: Required[Annotated[Dict[str, str], PropertyInfo(alias="engagementProperties")]]

    external_call_id: Required[Annotated[str, PropertyInfo(alias="externalCallId")]]

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

    from_number: Required[Annotated[FormattedPhoneNumberParam, PropertyInfo(alias="fromNumber")]]

    potential_recipient_user_ids: Required[Annotated[Iterable[int], PropertyInfo(alias="potentialRecipientUserIds")]]

    to_number: Required[Annotated[FormattedPhoneNumberParam, PropertyInfo(alias="toNumber")]]

    call_started_timestamp: Annotated[
        Union[str, datetime], PropertyInfo(alias="callStartedTimestamp", format="iso8601")
    ]

    duration_seconds: Annotated[int, PropertyInfo(alias="durationSeconds")]

    user_id: Annotated[int, PropertyInfo(alias="userId")]
