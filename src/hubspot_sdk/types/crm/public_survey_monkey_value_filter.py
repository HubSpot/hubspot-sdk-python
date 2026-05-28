# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union, Optional
from typing_extensions import Literal, Annotated, TypeAlias

from pydantic import Field as FieldInfo

from ..._utils import PropertyInfo
from ..._models import BaseModel
from .public_time_point_operation import PublicTimePointOperation
from .public_ranged_time_operation import PublicRangedTimeOperation
from .public_bool_property_operation import PublicBoolPropertyOperation
from .public_date_property_operation import PublicDatePropertyOperation
from .public_number_property_operation import PublicNumberPropertyOperation
from .public_string_property_operation import PublicStringPropertyOperation
from .public_all_property_types_operation import PublicAllPropertyTypesOperation
from .public_date_time_property_operation import PublicDateTimePropertyOperation
from .public_enumeration_property_operation import PublicEnumerationPropertyOperation
from .public_ranged_date_property_operation import PublicRangedDatePropertyOperation
from .public_multi_string_property_operation import PublicMultiStringPropertyOperation
from .public_calendar_date_property_operation import PublicCalendarDatePropertyOperation
from .public_ranged_number_property_operation import PublicRangedNumberPropertyOperation
from .public_rolling_property_updated_operation import PublicRollingPropertyUpdatedOperation
from .public_comparative_date_property_operation import PublicComparativeDatePropertyOperation
from .public_rolling_date_range_property_operation import PublicRollingDateRangePropertyOperation
from .public_comparative_property_updated_operation import PublicComparativePropertyUpdatedOperation

__all__ = ["PublicSurveyMonkeyValueFilter", "ValueComparison"]

ValueComparison: TypeAlias = Annotated[
    Union[
        PublicBoolPropertyOperation,
        PublicNumberPropertyOperation,
        PublicStringPropertyOperation,
        PublicDateTimePropertyOperation,
        PublicRangedDatePropertyOperation,
        PublicComparativePropertyUpdatedOperation,
        PublicComparativeDatePropertyOperation,
        PublicRollingDateRangePropertyOperation,
        PublicRollingPropertyUpdatedOperation,
        PublicEnumerationPropertyOperation,
        PublicAllPropertyTypesOperation,
        PublicRangedNumberPropertyOperation,
        PublicMultiStringPropertyOperation,
        PublicDatePropertyOperation,
        PublicCalendarDatePropertyOperation,
        PublicTimePointOperation,
        PublicRangedTimeOperation,
    ],
    PropertyInfo(discriminator="operation_type"),
]


class PublicSurveyMonkeyValueFilter(BaseModel):
    filter_type: Literal["SURVEY_MONKEY_VALUE"] = FieldInfo(alias="filterType")
    """Defines the type of filter (SURVEY_MONKEY_VALUE)."""

    operator: str
    """
    Defines the operation to be applied within the filter
    (HAS_ANSWERED_SURVEY_QUESTION_WITH_VALUE).
    """

    survey_id: str = FieldInfo(alias="surveyId")
    """The ID of the survey used in the filter."""

    survey_question: str = FieldInfo(alias="surveyQuestion")
    """The question from the survey used in the filter."""

    value_comparison: ValueComparison = FieldInfo(alias="valueComparison")
    """Specifies the operation used to compare the survey answer value."""

    survey_answer_col_id: Optional[str] = FieldInfo(alias="surveyAnswerColId", default=None)
    """The column ID of the survey answer used in the filter."""

    survey_answer_row_id: Optional[str] = FieldInfo(alias="surveyAnswerRowId", default=None)
    """The row ID of the survey answer used in the filter."""
