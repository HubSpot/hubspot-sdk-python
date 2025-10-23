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

__all__ = ["PublicEmailEventFilter", "PruningRefineBy"]

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


class PublicEmailEventFilter(TypedDict, total=False):
    app_id: Required[Annotated[str, PropertyInfo(alias="appId")]]

    email_id: Required[Annotated[str, PropertyInfo(alias="emailId")]]

    filter_type: Required[Annotated[Literal["EMAIL_EVENT"], PropertyInfo(alias="filterType")]]

    level: Required[str]

    operator: Required[
        Literal[
            "LINK_CLICKED",
            "MARKED_SPAM",
            "OPENED",
            "OPENED_BUT_LINK_NOT_CLICKED",
            "OPENED_BUT_NOT_REPLIED",
            "REPLIED",
            "UNSUBSCRIBED",
            "BOUNCED",
            "RECEIVED",
            "RECEIVED_BUT_NOT_OPENED",
            "SENT",
            "SENT_BUT_LINK_NOT_CLICKED",
            "SENT_BUT_NOT_RECEIVED",
        ]
    ]

    click_url: Annotated[str, PropertyInfo(alias="clickUrl")]

    pruning_refine_by: Annotated[PruningRefineBy, PropertyInfo(alias="pruningRefineBy")]
