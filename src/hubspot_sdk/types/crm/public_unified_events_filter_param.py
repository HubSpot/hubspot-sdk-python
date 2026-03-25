# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from ..._utils import PropertyInfo
from .public_time_point_operation_param import PublicTimePointOperationParam
from .public_all_history_refine_by_param import PublicAllHistoryRefineByParam
from .public_event_filter_metadata_param import PublicEventFilterMetadataParam
from .public_ranged_time_operation_param import PublicRangedTimeOperationParam
from .public_num_occurrences_refine_by_param import PublicNumOccurrencesRefineByParam
from .public_set_occurrences_refine_by_param import PublicSetOccurrencesRefineByParam
from .public_absolute_ranged_timestamp_refine_by_param import PublicAbsoluteRangedTimestampRefineByParam
from .public_relative_ranged_timestamp_refine_by_param import PublicRelativeRangedTimestampRefineByParam
from .public_absolute_comparative_timestamp_refine_by_param import PublicAbsoluteComparativeTimestampRefineByParam
from .public_relative_comparative_timestamp_refine_by_param import PublicRelativeComparativeTimestampRefineByParam

__all__ = ["PublicUnifiedEventsFilterParam", "CoalescingRefineBy", "PruningRefineBy"]

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


class PublicUnifiedEventsFilterParam(TypedDict, total=False):
    filter_lines: Required[Annotated[Iterable[PublicEventFilterMetadataParam], PropertyInfo(alias="filterLines")]]

    filter_type: Required[Annotated[Literal["UNIFIED_EVENTS"], PropertyInfo(alias="filterType")]]
    """Indicates the type of filter being applied (UNIFIED_EVENTS)."""

    coalescing_refine_by: Annotated[CoalescingRefineBy, PropertyInfo(alias="coalescingRefineBy")]
    """Specifies the criteria for refining the filter by coalescing."""

    event_type_id: Annotated[str, PropertyInfo(alias="eventTypeId")]
    """The identifier for the type of event in the unified events filter."""

    pruning_refine_by: Annotated[PruningRefineBy, PropertyInfo(alias="pruningRefineBy")]
    """Specifies the criteria for refining the filter by pruning."""
