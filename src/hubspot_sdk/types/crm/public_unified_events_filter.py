# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Literal, Annotated, TypeAlias

from pydantic import Field as FieldInfo

from ..._utils import PropertyInfo
from ..._models import BaseModel
from .public_time_point_operation import PublicTimePointOperation
from .public_all_history_refine_by import PublicAllHistoryRefineBy
from .public_event_filter_metadata import PublicEventFilterMetadata
from .public_ranged_time_operation import PublicRangedTimeOperation
from .public_num_occurrences_refine_by import PublicNumOccurrencesRefineBy
from .public_set_occurrences_refine_by import PublicSetOccurrencesRefineBy
from .public_absolute_ranged_timestamp_refine_by import PublicAbsoluteRangedTimestampRefineBy
from .public_relative_ranged_timestamp_refine_by import PublicRelativeRangedTimestampRefineBy
from .public_absolute_comparative_timestamp_refine_by import PublicAbsoluteComparativeTimestampRefineBy
from .public_relative_comparative_timestamp_refine_by import PublicRelativeComparativeTimestampRefineBy

__all__ = ["PublicUnifiedEventsFilter", "CoalescingRefineBy", "PruningRefineBy"]

CoalescingRefineBy: TypeAlias = Annotated[
    Union[
        PublicNumOccurrencesRefineBy,
        PublicSetOccurrencesRefineBy,
        PublicRelativeComparativeTimestampRefineBy,
        PublicRelativeRangedTimestampRefineBy,
        PublicAbsoluteComparativeTimestampRefineBy,
        PublicAbsoluteRangedTimestampRefineBy,
        PublicAllHistoryRefineBy,
        PublicTimePointOperation,
        PublicRangedTimeOperation,
    ],
    PropertyInfo(discriminator="type"),
]

PruningRefineBy: TypeAlias = Annotated[
    Union[
        PublicNumOccurrencesRefineBy,
        PublicSetOccurrencesRefineBy,
        PublicRelativeComparativeTimestampRefineBy,
        PublicRelativeRangedTimestampRefineBy,
        PublicAbsoluteComparativeTimestampRefineBy,
        PublicAbsoluteRangedTimestampRefineBy,
        PublicAllHistoryRefineBy,
        PublicTimePointOperation,
        PublicRangedTimeOperation,
    ],
    PropertyInfo(discriminator="type"),
]


class PublicUnifiedEventsFilter(BaseModel):
    filter_lines: List[PublicEventFilterMetadata] = FieldInfo(alias="filterLines")

    filter_type: Literal["UNIFIED_EVENTS"] = FieldInfo(alias="filterType")
    """Indicates the type of filter being applied (UNIFIED_EVENTS)."""

    coalescing_refine_by: Optional[CoalescingRefineBy] = FieldInfo(alias="coalescingRefineBy", default=None)
    """Specifies the criteria for refining the filter by coalescing."""

    event_type_id: Optional[str] = FieldInfo(alias="eventTypeId", default=None)
    """The identifier for the type of event in the unified events filter."""

    pruning_refine_by: Optional[PruningRefineBy] = FieldInfo(alias="pruningRefineBy", default=None)
    """Specifies the criteria for refining the filter by pruning."""
