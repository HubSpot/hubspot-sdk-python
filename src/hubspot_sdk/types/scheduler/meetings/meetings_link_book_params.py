# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from datetime import datetime
from typing_extensions import Required, Annotated, TypedDict

from ...._types import SequenceNotStr
from ...._utils import PropertyInfo
from ..external_booking_form_field_param import ExternalBookingFormFieldParam
from ..external_legal_consent_response_param import ExternalLegalConsentResponseParam

__all__ = ["MeetingsLinkBookParams"]


class MeetingsLinkBookParams(TypedDict, total=False):
    duration: Required[int]

    email: Required[str]

    first_name: Required[Annotated[str, PropertyInfo(alias="firstName")]]

    form_fields: Required[Annotated[Iterable[ExternalBookingFormFieldParam], PropertyInfo(alias="formFields")]]

    last_name: Required[Annotated[str, PropertyInfo(alias="lastName")]]

    legal_consent_responses: Required[
        Annotated[Iterable[ExternalLegalConsentResponseParam], PropertyInfo(alias="legalConsentResponses")]
    ]

    likely_available_user_ids: Required[Annotated[SequenceNotStr[str], PropertyInfo(alias="likelyAvailableUserIds")]]

    slug: Required[str]

    start_time: Required[Annotated[Union[str, datetime], PropertyInfo(alias="startTime", format="iso8601")]]

    locale: str

    timezone: str
