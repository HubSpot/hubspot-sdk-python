# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["PublicSurveyMonkeyFilter"]


class PublicSurveyMonkeyFilter(BaseModel):
    filter_type: Literal["SURVEY_MONKEY"] = FieldInfo(alias="filterType")
    """Indicates the type of filter being applied (SURVEY_MONKEY)."""

    operator: str
    """
    Specifies the operation to be performed by the filter (HAS_RESPONDED_TO_SURVEY,
    HAS_NOT_RESPONDED_TO_SURVEY).
    """

    survey_id: str = FieldInfo(alias="surveyId")
    """The ID of the survey associated with the filter."""
