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


class PublicEmailEventFilter(BaseModel):
    app_id: str = FieldInfo(alias="appId")
    """The ID of the application associated with the email event filter."""

    email_id: str = FieldInfo(alias="emailId")
    """The ID of the email associated with the event filter."""

    filter_type: Literal["EMAIL_EVENT"] = FieldInfo(alias="filterType")
    """Indicates the type of filter (EMAIL_EVENT)."""

    level: str
    """Specifies the level of the email event, such as EMAIL_API_CAMPAIGN_GROUP."""

    operator: Literal[
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
    """
    Defines the operation to be applied within the filter (BOUNCED, LINK_CLICKED,
    MARKED_SPAM, OPENED, OPENED_BUT_LINK_NOT_CLICKED, OPENED_BUT_NOT_REPLIED,
    RECEIVED, RECEIVED_BUT_NOT_OPENED, REPLIED, SENT, SENT_BUT_LINK_NOT_CLICKED,
    SENT_BUT_NOT_RECEIVED, UNSUBSCRIBED).
    """

    click_url: Optional[str] = FieldInfo(alias="clickUrl", default=None)
    """The URL that was clicked in the email event."""

    pruning_refine_by: Optional[PruningRefineBy] = FieldInfo(alias="pruningRefineBy", default=None)
    """Specifies the criteria for refining the filter by pruning."""
