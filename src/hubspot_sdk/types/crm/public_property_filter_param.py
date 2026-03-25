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

__all__ = ["PublicPropertyFilterParam", "Operation"]

Operation: TypeAlias = Union[
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


class PublicPropertyFilterParam(TypedDict, total=False):
    filter_type: Required[Annotated[Literal["PROPERTY"], PropertyInfo(alias="filterType")]]
    """Indicates that the filter (PROPERTY)."""

    operation: Required[Operation]
    """
    Defines the operation to be performed on the property, such as comparison or
    value matching.
    """

    property: Required[str]
    """Specifies the name of the property that the filter is applied to."""
