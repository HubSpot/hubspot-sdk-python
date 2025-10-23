# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["APIEnrollmentEventPropertyValueParam"]


class APIEnrollmentEventPropertyValueParam(TypedDict, total=False):
    enrollment_event_property_token: Required[Annotated[str, PropertyInfo(alias="enrollmentEventPropertyToken")]]

    type: Required[Literal["ENROLLMENT_EVENT_PROPERTY"]]
