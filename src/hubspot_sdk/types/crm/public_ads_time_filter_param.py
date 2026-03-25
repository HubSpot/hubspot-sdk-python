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

__all__ = ["PublicAdsTimeFilterParam", "PruningRefineBy"]

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


class PublicAdsTimeFilterParam(TypedDict, total=False):
    filter_type: Required[Annotated[Literal["ADS_TIME"], PropertyInfo(alias="filterType")]]
    """Filter type (ADS_TIME)"""

    pruning_refine_by: Required[Annotated[PruningRefineBy, PropertyInfo(alias="pruningRefineBy")]]
    """Refinement criteria"""
