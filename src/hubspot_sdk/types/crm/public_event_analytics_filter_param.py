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

__all__ = ["PublicEventAnalyticsFilterParam", "CoalescingRefineBy", "PruningRefineBy"]

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

PruningRefineBy: TypeAlias = Union[
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


class PublicEventAnalyticsFilterParam(TypedDict, total=False):
    event_id: Required[Annotated[str, PropertyInfo(alias="eventId")]]
    """The ID of the event to be used in the filter."""

    filter_type: Required[Annotated[Literal["EVENT"], PropertyInfo(alias="filterType")]]
    """Indicates the type of filter being applied (EVENT)."""

    operator: Required[str]
    """
    Defines the operation to be applied within the event filter (HAS_EVENT,
    NOT_HAS_EVENT).
    """

    coalescing_refine_by: Annotated[CoalescingRefineBy, PropertyInfo(alias="coalescingRefineBy")]
    """Specifies the criteria for refining the event filter by coalescing."""

    pruning_refine_by: Annotated[PruningRefineBy, PropertyInfo(alias="pruningRefineBy")]
    """Specifies the criteria for refining the event filter by pruning."""
