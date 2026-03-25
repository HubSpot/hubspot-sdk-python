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

__all__ = ["PublicAssociationInListFilterParam", "CoalescingRefineBy"]

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


class PublicAssociationInListFilterParam(TypedDict, total=False):
    association_category: Required[Annotated[str, PropertyInfo(alias="associationCategory")]]
    """
    Defines the category of the association, such as (HUBSPOT_DEFINED, USER_DEFINED,
    INTEGRATOR_DEFINED, WORK).
    """

    association_type_id: Required[Annotated[int, PropertyInfo(alias="associationTypeId")]]
    """The ID representing the type of association being filtered."""

    coalescing_refine_by: Required[Annotated[CoalescingRefineBy, PropertyInfo(alias="coalescingRefineBy")]]
    """Specifies the criteria for refining the association filter."""

    filter_type: Required[Annotated[Literal["ASSOCIATION"], PropertyInfo(alias="filterType")]]
    """Indicates the type of filter being applied, which is 'ASSOCIATION' by default."""

    list_id: Required[Annotated[str, PropertyInfo(alias="listId")]]
    """The ID of the list used in the association filter."""

    operator: Required[str]
    """
    Specifies the operation to be performed by the filter, such as 'IN_LIST' or
    'NOT_IN_LIST'.
    """

    to_object_type: Annotated[str, PropertyInfo(alias="toObjectType")]
    """The type of object that the association filter is targeting."""

    to_object_type_id: Annotated[str, PropertyInfo(alias="toObjectTypeId")]
    """
    The ID representing the type of object that the association filter is targeting.
    """
