# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union, Optional
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

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

__all__ = ["PublicFormSubmissionFilter", "CoalescingRefineBy", "PruningRefineBy"]

CoalescingRefineBy: TypeAlias = Union[
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


class PublicFormSubmissionFilter(BaseModel):
    filter_type: Literal["FORM_SUBMISSION"] = FieldInfo(alias="filterType")
    """Indicates the type of filter (FORM_SUBMISSION)."""

    operator: Literal["FILLED_OUT", "NOT_FILLED_OUT"]
    """Specifies the operation to be performed (FILLED_OUT, NOT_FILLED_OUT)."""

    coalescing_refine_by: Optional[CoalescingRefineBy] = FieldInfo(alias="coalescingRefineBy", default=None)
    """Specifies the criteria for refining the filter by coalescing."""

    form_id: Optional[str] = FieldInfo(alias="formId", default=None)
    """The ID of the form used in the filter."""

    pruning_refine_by: Optional[PruningRefineBy] = FieldInfo(alias="pruningRefineBy", default=None)
    """Specifies the criteria for refining the filter by pruning."""
