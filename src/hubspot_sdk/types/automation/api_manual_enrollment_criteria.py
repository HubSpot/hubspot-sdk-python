# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["APIManualEnrollmentCriteria"]


class APIManualEnrollmentCriteria(BaseModel):
    should_re_enroll: bool = FieldInfo(alias="shouldReEnroll")
    """Whether or not the same object can enroll in this workflow twice."""

    type: Literal["MANUAL"]
    """
    The type of enrollment criteria this is, this can be "LIST_BASED",
    "EVENT_BASED", or "MANUAL".
    """
