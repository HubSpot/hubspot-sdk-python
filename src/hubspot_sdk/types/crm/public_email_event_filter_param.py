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

__all__ = ["PublicEmailEventFilterParam", "PruningRefineBy"]

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


class PublicEmailEventFilterParam(TypedDict, total=False):
    app_id: Required[Annotated[str, PropertyInfo(alias="appId")]]
    """The ID of the application associated with the email event filter."""

    email_id: Required[Annotated[str, PropertyInfo(alias="emailId")]]
    """The ID of the email associated with the event filter."""

    filter_type: Required[Annotated[Literal["EMAIL_EVENT"], PropertyInfo(alias="filterType")]]
    """Indicates the type of filter (EMAIL_EVENT)."""

    level: Required[str]
    """Specifies the level of the email event, such as EMAIL_API_CAMPAIGN_GROUP."""

    operator: Required[
        Literal[
            "BOUNCED",
            "LINK_CLICKED",
            "MARKED_SPAM",
            "OPENED",
            "OPENED_BUT_LINK_NOT_CLICKED",
            "OPENED_BUT_NOT_REPLIED",
            "RECEIVED",
            "RECEIVED_BUT_NOT_OPENED",
            "REPLIED",
            "SENT",
            "SENT_BUT_LINK_NOT_CLICKED",
            "SENT_BUT_NOT_RECEIVED",
            "UNSUBSCRIBED",
        ]
    ]
    """
    Defines the operation to be applied within the filter (BOUNCED, LINK_CLICKED,
    MARKED_SPAM, OPENED, OPENED_BUT_LINK_NOT_CLICKED, OPENED_BUT_NOT_REPLIED,
    RECEIVED, RECEIVED_BUT_NOT_OPENED, REPLIED, SENT, SENT_BUT_LINK_NOT_CLICKED,
    SENT_BUT_NOT_RECEIVED, UNSUBSCRIBED).
    """

    click_url: Annotated[str, PropertyInfo(alias="clickUrl")]
    """The URL that was clicked in the email event."""

    pruning_refine_by: Annotated[PruningRefineBy, PropertyInfo(alias="pruningRefineBy")]
    """Specifies the criteria for refining the filter by pruning."""
