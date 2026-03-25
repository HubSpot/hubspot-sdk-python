# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from datetime import datetime
from typing_extensions import Required, Annotated, TypedDict

from ...._types import SequenceNotStr
from ...._utils import PropertyInfo
from ..external_booking_form_field_param import ExternalBookingFormFieldParam
from ..external_legal_consent_response_param import ExternalLegalConsentResponseParam

__all__ = ["AdvancedBookParams"]


class AdvancedBookParams(TypedDict, total=False):
    duration: Required[int]
    """The duration of the meeting in milliseconds."""

    email: Required[str]
    """The email address of the person booking the meeting."""

    first_name: Required[Annotated[str, PropertyInfo(alias="firstName")]]
    """The first name of the person booking the meeting."""

    form_fields: Required[Annotated[Iterable[ExternalBookingFormFieldParam], PropertyInfo(alias="formFields")]]

    last_name: Required[Annotated[str, PropertyInfo(alias="lastName")]]
    """The last name of the person booking the meeting."""

    legal_consent_responses: Required[
        Annotated[Iterable[ExternalLegalConsentResponseParam], PropertyInfo(alias="legalConsentResponses")]
    ]

    likely_available_user_ids: Required[Annotated[SequenceNotStr[str], PropertyInfo(alias="likelyAvailableUserIds")]]

    slug: Required[str]
    """The unique path identifier for the meeting page."""

    start_time: Required[Annotated[Union[str, datetime], PropertyInfo(alias="startTime", format="iso8601")]]
    """The date and time when the meeting is scheduled to start, in ISO 8601 format."""

    locale: str
    """The locale used for formatting dates and times in the meeting booking."""

    timezone: str
    """The timezone in which the meeting is scheduled."""
