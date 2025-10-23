# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["PublicSurveyMonkeyFilter"]


class PublicSurveyMonkeyFilter(BaseModel):
    filter_type: Literal["SURVEY_MONKEY"] = FieldInfo(alias="filterType")

    operator: str

    survey_id: str = FieldInfo(alias="surveyId")
