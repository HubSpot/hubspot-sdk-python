# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from ..._utils import PropertyInfo
from .public_time_point_operation_param import PublicTimePointOperationParam
from .public_ranged_time_operation_param import PublicRangedTimeOperationParam
from .public_bool_property_operation_param import PublicBoolPropertyOperationParam
from .public_date_property_operation_param import PublicDatePropertyOperationParam
from .public_number_property_operation_param import PublicNumberPropertyOperationParam
from .public_string_property_operation_param import PublicStringPropertyOperationParam
from .public_all_property_types_operation_param import PublicAllPropertyTypesOperationParam
from .public_date_time_property_operation_param import PublicDateTimePropertyOperationParam
from .public_enumeration_property_operation_param import PublicEnumerationPropertyOperationParam
from .public_ranged_date_property_operation_param import PublicRangedDatePropertyOperationParam
from .public_multi_string_property_operation_param import PublicMultiStringPropertyOperationParam
from .public_calendar_date_property_operation_param import PublicCalendarDatePropertyOperationParam
from .public_ranged_number_property_operation_param import PublicRangedNumberPropertyOperationParam
from .public_rolling_property_updated_operation_param import PublicRollingPropertyUpdatedOperationParam
from .public_comparative_date_property_operation_param import PublicComparativeDatePropertyOperationParam
from .public_rolling_date_range_property_operation_param import PublicRollingDateRangePropertyOperationParam
from .public_comparative_property_updated_operation_param import PublicComparativePropertyUpdatedOperationParam

__all__ = ["PublicSurveyMonkeyValueFilterParam", "ValueComparison"]

ValueComparison: TypeAlias = Union[
    PublicBoolPropertyOperationParam,
    PublicNumberPropertyOperationParam,
    PublicStringPropertyOperationParam,
    PublicDateTimePropertyOperationParam,
    PublicRangedDatePropertyOperationParam,
    PublicComparativePropertyUpdatedOperationParam,
    PublicComparativeDatePropertyOperationParam,
    PublicRollingDateRangePropertyOperationParam,
    PublicRollingPropertyUpdatedOperationParam,
    PublicEnumerationPropertyOperationParam,
    PublicAllPropertyTypesOperationParam,
    PublicRangedNumberPropertyOperationParam,
    PublicMultiStringPropertyOperationParam,
    PublicDatePropertyOperationParam,
    PublicCalendarDatePropertyOperationParam,
    PublicTimePointOperationParam,
    PublicRangedTimeOperationParam,
]


class PublicSurveyMonkeyValueFilterParam(TypedDict, total=False):
    filter_type: Required[Annotated[Literal["SURVEY_MONKEY_VALUE"], PropertyInfo(alias="filterType")]]
    """Defines the type of filter (SURVEY_MONKEY_VALUE)."""

    operator: Required[str]
    """
    Defines the operation to be applied within the filter
    (HAS_ANSWERED_SURVEY_QUESTION_WITH_VALUE).
    """

    survey_id: Required[Annotated[str, PropertyInfo(alias="surveyId")]]
    """The ID of the survey used in the filter."""

    survey_question: Required[Annotated[str, PropertyInfo(alias="surveyQuestion")]]
    """The question from the survey used in the filter."""

    value_comparison: Required[Annotated[ValueComparison, PropertyInfo(alias="valueComparison")]]
    """Specifies the operation used to compare the survey answer value."""

    survey_answer_col_id: Annotated[str, PropertyInfo(alias="surveyAnswerColId")]
    """The column ID of the survey answer used in the filter."""

    survey_answer_row_id: Annotated[str, PropertyInfo(alias="surveyAnswerRowId")]
    """The row ID of the survey answer used in the filter."""
