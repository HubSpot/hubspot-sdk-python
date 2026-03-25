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

__all__ = ["PublicCtaAnalyticsFilterParam", "CoalescingRefineBy", "PruningRefineBy"]

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


class PublicCtaAnalyticsFilterParam(TypedDict, total=False):
    cta_name: Required[Annotated[str, PropertyInfo(alias="ctaName")]]
    """The name of the Call-to-Action (CTA) to be used in the filter."""

    filter_type: Required[Annotated[Literal["CTA"], PropertyInfo(alias="filterType")]]
    """Indicates the type of filter being applied, which is (CTA)."""

    operator: Required[str]
    """
    Defines the operation to be applied within the filter (HAS_CLICKED_CTA,
    HAS_NOT_CLICKED_CTA, HAS_OPENED_CTA, HAS_NOT_OPENED_CTA,
    HAS_CLICKED_CTA_PLACEMENT, HAS_NOT_CLICKED_CTA_PLACEMENT,
    HAS_OPENED_CTA_PLACEMENT, HAS_NOT_OPENED_CTA_PLACEMENT).
    """

    coalescing_refine_by: Annotated[CoalescingRefineBy, PropertyInfo(alias="coalescingRefineBy")]
    """Specifies the criteria for refining the filter by coalescing."""

    pruning_refine_by: Annotated[PruningRefineBy, PropertyInfo(alias="pruningRefineBy")]
    """Specifies the criteria for refining the filter by pruning."""
