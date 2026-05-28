# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union, Optional
from typing_extensions import Literal, Annotated, TypeAlias

from pydantic import Field as FieldInfo

from ..._utils import PropertyInfo
from ..._models import BaseModel
from .time_point_operation import TimePointOperation
from .ranged_time_operation import RangedTimeOperation
from .bool_property_operation import BoolPropertyOperation
from .date_property_operation import DatePropertyOperation
from .property_filter_context import PropertyFilterContext
from .regex_property_operation import RegexPropertyOperation
from .number_property_operation import NumberPropertyOperation
from .string_property_operation import StringPropertyOperation
from .all_property_types_operation import AllPropertyTypesOperation
from .date_time_property_operation import DateTimePropertyOperation
from .enumeration_property_operation import EnumerationPropertyOperation
from .ranged_date_property_operation import RangedDatePropertyOperation
from .multi_string_property_operation import MultiStringPropertyOperation
from .calendar_date_property_operation import CalendarDatePropertyOperation
from .ranged_number_property_operation import RangedNumberPropertyOperation
from .rolling_property_updated_operation import RollingPropertyUpdatedOperation
from .comparative_bool_property_operation import ComparativeBoolPropertyOperation
from .comparative_date_property_operation import ComparativeDatePropertyOperation
from .comparative_number_property_operation import ComparativeNumberPropertyOperation
from .comparative_string_property_operation import ComparativeStringPropertyOperation
from .rolling_date_range_property_operation import RollingDateRangePropertyOperation
from .comparative_property_updated_operation import ComparativePropertyUpdatedOperation

__all__ = ["PropertyFilter", "Operation"]

Operation: TypeAlias = Annotated[
    Union[
        BoolPropertyOperation,
        NumberPropertyOperation,
        StringPropertyOperation,
        DateTimePropertyOperation,
        RangedDatePropertyOperation,
        ComparativeDatePropertyOperation,
        ComparativeBoolPropertyOperation,
        ComparativeNumberPropertyOperation,
        ComparativeStringPropertyOperation,
        ComparativePropertyUpdatedOperation,
        RollingDateRangePropertyOperation,
        RollingPropertyUpdatedOperation,
        EnumerationPropertyOperation,
        AllPropertyTypesOperation,
        RangedNumberPropertyOperation,
        MultiStringPropertyOperation,
        DatePropertyOperation,
        CalendarDatePropertyOperation,
        TimePointOperation,
        RangedTimeOperation,
        RegexPropertyOperation,
    ],
    PropertyInfo(discriminator="property_type"),
]


class PropertyFilter(BaseModel):
    filter_type: Literal["PROPERTY"] = FieldInfo(alias="filterType")

    operation: Operation

    property: str

    context: Optional[PropertyFilterContext] = None

    filter_insights_id: Optional[int] = FieldInfo(alias="filterInsightsId", default=None)

    framework_filter_id: Optional[int] = FieldInfo(alias="frameworkFilterId", default=None)
