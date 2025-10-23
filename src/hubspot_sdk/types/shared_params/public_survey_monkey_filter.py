# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["PublicSurveyMonkeyFilter"]


class PublicSurveyMonkeyFilter(TypedDict, total=False):
    filter_type: Required[Annotated[Literal["SURVEY_MONKEY"], PropertyInfo(alias="filterType")]]

    operator: Required[str]

    survey_id: Required[Annotated[str, PropertyInfo(alias="surveyId")]]
