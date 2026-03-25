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

__all__ = ["PublicPropertyAssociationInListFilter", "CoalescingRefineBy"]

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


class PublicPropertyAssociationInListFilter(BaseModel):
    coalescing_refine_by: CoalescingRefineBy = FieldInfo(alias="coalescingRefineBy")
    """Specifies the criteria for refining the filter by coalescing."""

    filter_type: Literal["PROPERTY_ASSOCIATION"] = FieldInfo(alias="filterType")
    """Indicates the type of filter being applied (PROPERTY_ASSOCIATION)."""

    list_id: str = FieldInfo(alias="listId")
    """The ID of the list used in the property association filter."""

    operator: str
    """Defines the operation to be applied by the filter (IN_LIST, NOT_IN_LIST)."""

    property_with_object_id: str = FieldInfo(alias="propertyWithObjectId")
    """The property associated with the object ID in the filter."""

    to_object_type_id: Optional[str] = FieldInfo(alias="toObjectTypeId", default=None)
    """
    The ID representing the type of object that the property association filter is
    targeting.
    """
