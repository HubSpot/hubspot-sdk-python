# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["APIEnrollmentEventPropertyValue"]


class APIEnrollmentEventPropertyValue(BaseModel):
    enrollment_event_property_token: str = FieldInfo(alias="enrollmentEventPropertyToken")

    type: Literal["ENROLLMENT_EVENT_PROPERTY"]
