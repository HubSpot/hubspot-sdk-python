# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Literal, Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo

__all__ = ["EmailListParams"]


class EmailListParams(TypedDict, total=False):
    after: str
    """The cursor token value to get the next set of results.

    You can get this from the `paging.next.after` JSON property of a paged response
    containing more results.
    """

    archived: bool
    """Specifies whether to return archived emails. Defaults to `false`."""

    campaign: str
    """Filter by campaign GUID. All emails will be returned if not present."""

    created_after: Annotated[Union[str, datetime], PropertyInfo(alias="createdAfter", format="iso8601")]
    """Only return emails created after the specified time."""

    created_at: Annotated[Union[str, datetime], PropertyInfo(alias="createdAt", format="iso8601")]
    """Only return emails created at exactly the specified time."""

    created_before: Annotated[Union[str, datetime], PropertyInfo(alias="createdBefore", format="iso8601")]
    """Only return emails created before the specified time."""

    included_properties: Annotated[SequenceNotStr[str], PropertyInfo(alias="includedProperties")]
    """Limit the response to only include this specified list of properties."""

    include_stats: Annotated[bool, PropertyInfo(alias="includeStats")]
    """Include statistics with emails."""

    is_published: Annotated[bool, PropertyInfo(alias="isPublished")]
    """Filter by published/draft emails. All emails will be returned if not present."""

    limit: int
    """The maximum number of results to return. Default is 10."""

    marketing_campaign_names: Annotated[bool, PropertyInfo(alias="marketingCampaignNames")]
    """Include the names for any associated marketing campaigns."""

    sort: SequenceNotStr[str]
    """Specifies which fields to use for sorting results.

    Valid fields are `name`, `createdAt`, `updatedAt`, `createdBy`, `updatedBy`.
    `createdAt` will be used by default.
    """

    type: Literal[
        "AB_EMAIL",
        "BATCH_EMAIL",
        "LOCALTIME_EMAIL",
        "AUTOMATED_AB_EMAIL",
        "BLOG_EMAIL",
        "BLOG_EMAIL_CHILD",
        "RSS_EMAIL",
        "RSS_EMAIL_CHILD",
        "RESUBSCRIBE_EMAIL",
        "OPTIN_EMAIL",
        "OPTIN_FOLLOWUP_EMAIL",
        "AUTOMATED_EMAIL",
        "FEEDBACK_CES_EMAIL",
        "FEEDBACK_CUSTOM_EMAIL",
        "FEEDBACK_CUSTOM_SURVEY_EMAIL",
        "FEEDBACK_NPS_EMAIL",
        "FOLLOWUP_EMAIL",
        "LEADFLOW_EMAIL",
        "SINGLE_SEND_API",
        "MARKETING_SINGLE_SEND_API",
        "SMTP_TOKEN",
        "TICKET_EMAIL",
        "MEMBERSHIP_REGISTRATION_EMAIL",
        "MEMBERSHIP_PASSWORD_SAVED_EMAIL",
        "MEMBERSHIP_PASSWORD_RESET_EMAIL",
        "MEMBERSHIP_EMAIL_VERIFICATION_EMAIL",
        "MEMBERSHIP_PASSWORDLESS_AUTH_EMAIL",
        "MEMBERSHIP_REGISTRATION_FOLLOW_UP_EMAIL",
        "MEMBERSHIP_OTP_LOGIN_EMAIL",
        "MEMBERSHIP_FOLLOW_UP_EMAIL",
        "MEMBERSHIP_VERIFICATION_EMAIL",
    ]
    """Email types to be filtered by.

    Multiple types can be included. All emails will be returned if not present.
    """

    updated_after: Annotated[Union[str, datetime], PropertyInfo(alias="updatedAfter", format="iso8601")]
    """Only return emails last updated after the specified time."""

    updated_at: Annotated[Union[str, datetime], PropertyInfo(alias="updatedAt", format="iso8601")]
    """Only return emails last updated at exactly the specified time."""

    updated_before: Annotated[Union[str, datetime], PropertyInfo(alias="updatedBefore", format="iso8601")]
    """Only return emails last updated before the specified time."""

    workflow_names: Annotated[bool, PropertyInfo(alias="workflowNames")]
    """Include the names of any workflows associated with the returned emails."""
