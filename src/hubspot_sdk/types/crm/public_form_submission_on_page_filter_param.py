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

__all__ = ["PublicFormSubmissionOnPageFilterParam", "CoalescingRefineBy", "PruningRefineBy"]

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


class PublicFormSubmissionOnPageFilterParam(TypedDict, total=False):
    filter_type: Required[Annotated[Literal["FORM_SUBMISSION_ON_PAGE"], PropertyInfo(alias="filterType")]]
    """Indicates the type of filter (FORM_SUBMISSION_ON_PAGE)."""

    operator: Required[Literal["FILLED_OUT", "NOT_FILLED_OUT"]]
    """Specifies the operation to be applied (FILLED_OUT, NOT_FILLED_OUT)."""

    page_id: Required[Annotated[str, PropertyInfo(alias="pageId")]]
    """The ID of the page where the form submission occurred."""

    coalescing_refine_by: Annotated[CoalescingRefineBy, PropertyInfo(alias="coalescingRefineBy")]
    """Defines the criteria for refining the filter by coalescing."""

    form_id: Annotated[str, PropertyInfo(alias="formId")]
    """The ID of the form associated with the submission filter."""

    pruning_refine_by: Annotated[PruningRefineBy, PropertyInfo(alias="pruningRefineBy")]
    """Specifies the criteria for refining the filter by pruning."""
