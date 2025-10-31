# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["APIManualEnrollmentCriteria"]


class APIManualEnrollmentCriteria(BaseModel):
    should_re_enroll: bool = FieldInfo(alias="shouldReEnroll")

    type: Literal["MANUAL"]
