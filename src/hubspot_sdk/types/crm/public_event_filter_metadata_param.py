# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Required, TypeAlias, TypedDict

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

__all__ = ["PublicEventFilterMetadataParam", "Operation"]

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


class PublicEventFilterMetadataParam(TypedDict, total=False):
    operation: Required[Operation]
    """Defines the operation to be performed on the property"""

    property: Required[str]
    """Specifies the property on which the operation is to be applied."""
