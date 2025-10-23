# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from ..._utils import PropertyInfo
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

__all__ = ["PublicPropertyFilter", "Operation"]

Operation: TypeAlias = Union[
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
]


class PublicPropertyFilter(TypedDict, total=False):
    filter_type: Required[Annotated[Literal["PROPERTY"], PropertyInfo(alias="filterType")]]

    operation: Required[Operation]

    property: Required[str]
