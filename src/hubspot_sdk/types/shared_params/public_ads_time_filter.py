# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from ..._utils import PropertyInfo
from .public_time_point_operation import PublicTimePointOperation
from .public_all_history_refine_by import PublicAllHistoryRefineBy
from .public_ranged_time_operation import PublicRangedTimeOperation
from .public_num_occurrences_refine_by import PublicNumOccurrencesRefineBy
from .public_set_occurrences_refine_by import PublicSetOccurrencesRefineBy
from .public_absolute_ranged_timestamp_refine_by import PublicAbsoluteRangedTimestampRefineBy
from .public_relative_ranged_timestamp_refine_by import PublicRelativeRangedTimestampRefineBy
from .public_absolute_comparative_timestamp_refine_by import PublicAbsoluteComparativeTimestampRefineBy
from .public_relative_comparative_timestamp_refine_by import PublicRelativeComparativeTimestampRefineBy

__all__ = ["PublicAdsTimeFilter", "PruningRefineBy"]

PruningRefineBy: TypeAlias = Union[
    PublicNumOccurrencesRefineBy,
    PublicSetOccurrencesRefineBy,
    PublicRelativeComparativeTimestampRefineBy,
    PublicRelativeRangedTimestampRefineBy,
    PublicAbsoluteComparativeTimestampRefineBy,
    PublicAbsoluteRangedTimestampRefineBy,
    PublicAllHistoryRefineBy,
    PublicTimePointOperation,
    PublicRangedTimeOperation,
]


class PublicAdsTimeFilter(TypedDict, total=False):
    filter_type: Required[Annotated[Literal["ADS_TIME"], PropertyInfo(alias="filterType")]]

    pruning_refine_by: Required[Annotated[PruningRefineBy, PropertyInfo(alias="pruningRefineBy")]]
