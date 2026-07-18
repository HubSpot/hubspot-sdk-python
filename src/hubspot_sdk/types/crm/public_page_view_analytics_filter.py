# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union, Optional
from typing_extensions import Literal, Annotated, TypeAlias

from pydantic import Field as FieldInfo

from ..._utils import PropertyInfo
from ..._models import BaseModel
from .public_time_point_operation import PublicTimePointOperation
from .public_all_history_refine_by import PublicAllHistoryRefineBy
from .public_ranged_time_operation import PublicRangedTimeOperation
from .public_num_occurrences_refine_by import PublicNumOccurrencesRefineBy
from .public_set_occurrences_refine_by import PublicSetOccurrencesRefineBy
from .public_absolute_ranged_timestamp_refine_by import PublicAbsoluteRangedTimestampRefineBy
from .public_relative_ranged_timestamp_refine_by import PublicRelativeRangedTimestampRefineBy
from .public_absolute_comparative_timestamp_refine_by import PublicAbsoluteComparativeTimestampRefineBy
from .public_relative_comparative_timestamp_refine_by import PublicRelativeComparativeTimestampRefineBy

__all__ = ["PublicPageViewAnalyticsFilter", "CoalescingRefineBy", "PruningRefineBy"]

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


class PublicPageViewAnalyticsFilter(BaseModel):
    filter_type: Literal["PAGE_VIEW"] = FieldInfo(alias="filterType")
    """Indicates the type of filter being applied (PAGE_VIEW)."""

    operator: str
    """
    Defines the operation to be applied within the filter (HAS_PAGEVIEW_EQ,
    HAS_PAGEVIEW_CONTAINS, HAS_PAGEVIEW_MATCHES_REGEX, NOT_HAS_PAGEVIEW_EQ,
    NOT_HAS_PAGEVIEW_CONTAINS).
    """

    page_url: str = FieldInfo(alias="pageUrl")
    """The URL of the page to be used in the filter."""

    coalescing_refine_by: Optional[CoalescingRefineBy] = FieldInfo(alias="coalescingRefineBy", default=None)
    """Specifies the criteria for refining the filter by coalescing."""

    enable_tracking: Optional[bool] = FieldInfo(alias="enableTracking", default=None)
    """Indicates whether tracking is enabled for the page view."""

    pruning_refine_by: Optional[PruningRefineBy] = FieldInfo(alias="pruningRefineBy", default=None)
    """Specifies the criteria for refining the filter by pruning."""
