# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from ..._utils import PropertyInfo
from .public_time_point_operation_param import PublicTimePointOperationParam
from .public_all_history_refine_by_param import PublicAllHistoryRefineByParam
from .public_ranged_time_operation_param import PublicRangedTimeOperationParam
from .public_num_occurrences_refine_by_param import PublicNumOccurrencesRefineByParam
from .public_set_occurrences_refine_by_param import PublicSetOccurrencesRefineByParam
from .public_absolute_ranged_timestamp_refine_by_param import PublicAbsoluteRangedTimestampRefineByParam
from .public_relative_ranged_timestamp_refine_by_param import PublicRelativeRangedTimestampRefineByParam
from .public_absolute_comparative_timestamp_refine_by_param import PublicAbsoluteComparativeTimestampRefineByParam
from .public_relative_comparative_timestamp_refine_by_param import PublicRelativeComparativeTimestampRefineByParam

__all__ = ["PublicPropertyAssociationInListFilterParam", "CoalescingRefineBy"]

CoalescingRefineBy: TypeAlias = Union[
    PublicNumOccurrencesRefineByParam,
    PublicSetOccurrencesRefineByParam,
    PublicRelativeComparativeTimestampRefineByParam,
    PublicRelativeRangedTimestampRefineByParam,
    PublicAbsoluteComparativeTimestampRefineByParam,
    PublicAbsoluteRangedTimestampRefineByParam,
    PublicAllHistoryRefineByParam,
    PublicTimePointOperationParam,
    PublicRangedTimeOperationParam,
]


class PublicPropertyAssociationInListFilterParam(TypedDict, total=False):
    coalescing_refine_by: Required[Annotated[CoalescingRefineBy, PropertyInfo(alias="coalescingRefineBy")]]
    """Specifies the criteria for refining the filter by coalescing."""

    filter_type: Required[Annotated[Literal["PROPERTY_ASSOCIATION"], PropertyInfo(alias="filterType")]]
    """Indicates the type of filter being applied (PROPERTY_ASSOCIATION)."""

    list_id: Required[Annotated[str, PropertyInfo(alias="listId")]]
    """The ID of the list used in the property association filter."""

    operator: Required[str]
    """Defines the operation to be applied by the filter (IN_LIST, NOT_IN_LIST)."""

    property_with_object_id: Required[Annotated[str, PropertyInfo(alias="propertyWithObjectId")]]
    """The property associated with the object ID in the filter."""

    to_object_type_id: Annotated[str, PropertyInfo(alias="toObjectTypeId")]
    """
    The ID representing the type of object that the property association filter is
    targeting.
    """
