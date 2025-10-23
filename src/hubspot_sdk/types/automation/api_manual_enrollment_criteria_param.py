# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["APIManualEnrollmentCriteriaParam"]


class APIManualEnrollmentCriteriaParam(TypedDict, total=False):
    should_re_enroll: Required[Annotated[bool, PropertyInfo(alias="shouldReEnroll")]]
    """Whether or not the same object can enroll in this workflow twice."""

    type: Required[Literal["MANUAL"]]
    """
    The type of enrollment criteria this is, this can be "LIST_BASED",
    "EVENT_BASED", or "MANUAL".
    """
