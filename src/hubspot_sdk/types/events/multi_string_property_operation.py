# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Literal, Annotated, TypeAlias

from pydantic import Field as FieldInfo

from ..._utils import PropertyInfo
from ..._models import BaseModel
from .time_point_operation import TimePointOperation
from .all_history_refine_by import AllHistoryRefineBy
from .ranged_time_operation import RangedTimeOperation
from .num_occurrences_refine_by import NumOccurrencesRefineBy
from .set_occurrences_refine_by import SetOccurrencesRefineBy
from .absolute_ranged_timestamp_refine_by import AbsoluteRangedTimestampRefineBy
from .relative_ranged_timestamp_refine_by import RelativeRangedTimestampRefineBy
from .absolute_comparative_timestamp_refine_by import AbsoluteComparativeTimestampRefineBy
from .relative_comparative_timestamp_refine_by import RelativeComparativeTimestampRefineBy

__all__ = ["MultiStringPropertyOperation", "CoalescingRefineBy", "PruningRefineBy"]

CoalescingRefineBy: TypeAlias = Annotated[
    Union[NumOccurrencesRefineBy, SetOccurrencesRefineBy], PropertyInfo(discriminator="type")
]

PruningRefineBy: TypeAlias = Annotated[
    Union[
        RelativeComparativeTimestampRefineBy,
        RelativeRangedTimestampRefineBy,
        AbsoluteComparativeTimestampRefineBy,
        AbsoluteRangedTimestampRefineBy,
        AllHistoryRefineBy,
        TimePointOperation,
        RangedTimeOperation,
    ],
    PropertyInfo(discriminator="type"),
]


class MultiStringPropertyOperation(BaseModel):
    coalescing_refine_by: CoalescingRefineBy = FieldInfo(alias="coalescingRefineBy")

    include_objects_with_no_value_set: bool = FieldInfo(alias="includeObjectsWithNoValueSet")

    operation_type: str = FieldInfo(alias="operationType")

    operator: Literal[
        "CONTAINS",
        "CONTAINS_EXACTLY",
        "DOES_NOT_CONTAIN",
        "DOES_NOT_CONTAIN_EXACTLY",
        "ENDS_WITH",
        "IS_EQUAL_TO",
        "IS_NOT_EQUAL_TO",
        "STARTS_WITH",
    ]

    operator_name: str = FieldInfo(alias="operatorName")

    property_type: Literal["multistring"] = FieldInfo(alias="propertyType")

    values: List[str]

    default_value: Optional[str] = FieldInfo(alias="defaultValue", default=None)

    pruning_refine_by: Optional[PruningRefineBy] = FieldInfo(alias="pruningRefineBy", default=None)

    render_spec: Optional[str] = FieldInfo(alias="renderSpec", default=None)
