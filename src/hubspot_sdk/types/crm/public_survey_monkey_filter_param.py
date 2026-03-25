# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["PublicSurveyMonkeyFilterParam"]


class PublicSurveyMonkeyFilterParam(TypedDict, total=False):
    filter_type: Required[Annotated[Literal["SURVEY_MONKEY"], PropertyInfo(alias="filterType")]]
    """Indicates the type of filter being applied (SURVEY_MONKEY)."""

    operator: Required[str]
    """
    Specifies the operation to be performed by the filter (HAS_RESPONDED_TO_SURVEY,
    HAS_NOT_RESPONDED_TO_SURVEY).
    """

    survey_id: Required[Annotated[str, PropertyInfo(alias="surveyId")]]
    """The ID of the survey associated with the filter."""
