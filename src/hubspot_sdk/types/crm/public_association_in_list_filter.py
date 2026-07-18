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

__all__ = ["PublicAssociationInListFilter", "CoalescingRefineBy"]

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


class PublicAssociationInListFilter(BaseModel):
    association_category: str = FieldInfo(alias="associationCategory")
    """
    Defines the category of the association, such as (HUBSPOT_DEFINED, USER_DEFINED,
    INTEGRATOR_DEFINED, WORK).
    """

    association_type_id: int = FieldInfo(alias="associationTypeId")
    """The ID representing the type of association being filtered."""

    coalescing_refine_by: CoalescingRefineBy = FieldInfo(alias="coalescingRefineBy")
    """Specifies the criteria for refining the association filter."""

    filter_type: Literal["ASSOCIATION"] = FieldInfo(alias="filterType")
    """Indicates the type of filter being applied, which is 'ASSOCIATION' by default."""

    list_id: str = FieldInfo(alias="listId")
    """The ID of the list used in the association filter."""

    operator: str
    """
    Specifies the operation to be performed by the filter, such as 'IN_LIST' or
    'NOT_IN_LIST'.
    """

    to_object_type: Optional[str] = FieldInfo(alias="toObjectType", default=None)
    """The type of object that the association filter is targeting."""

    to_object_type_id: Optional[str] = FieldInfo(alias="toObjectTypeId", default=None)
    """
    The ID representing the type of object that the association filter is targeting.
    """
