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
    """
    The paging cursor token of the last successfully read resource will be returned
    as the `paging.next.after` JSON property of a paged response containing more
    results.
    """

    archived: bool
    """Whether to return only results that have been archived."""

    campaign: str

    created_after: Annotated[Union[str, datetime], PropertyInfo(alias="createdAfter", format="iso8601")]

    created_at: Annotated[Union[str, datetime], PropertyInfo(alias="createdAt", format="iso8601")]

    created_before: Annotated[Union[str, datetime], PropertyInfo(alias="createdBefore", format="iso8601")]

    included_properties: Annotated[SequenceNotStr[str], PropertyInfo(alias="includedProperties")]

    include_stats: Annotated[bool, PropertyInfo(alias="includeStats")]

    is_published: Annotated[bool, PropertyInfo(alias="isPublished")]

    limit: int
    """The maximum number of results to display per page."""

    marketing_campaign_names: Annotated[bool, PropertyInfo(alias="marketingCampaignNames")]

    published_after: Annotated[Union[str, datetime], PropertyInfo(alias="publishedAfter", format="iso8601")]

    published_at: Annotated[Union[str, datetime], PropertyInfo(alias="publishedAt", format="iso8601")]

    published_before: Annotated[Union[str, datetime], PropertyInfo(alias="publishedBefore", format="iso8601")]

    sort: SequenceNotStr[str]

    type: Literal[
        "AB_EMAIL",
        "AUTOMATED_AB_EMAIL",
        "AUTOMATED_EMAIL",
        "BATCH_EMAIL",
        "BLOG_EMAIL",
        "BLOG_EMAIL_CHILD",
        "FEEDBACK_CES_EMAIL",
        "FEEDBACK_CUSTOM_EMAIL",
        "FEEDBACK_CUSTOM_SURVEY_EMAIL",
        "FEEDBACK_NPS_EMAIL",
        "FOLLOWUP_EMAIL",
        "LEADFLOW_EMAIL",
        "LOCALTIME_EMAIL",
        "MANAGE_PREFERENCES_EMAIL",
        "MARKETING_SINGLE_SEND_API",
        "MEMBERSHIP_EMAIL_VERIFICATION_EMAIL",
        "MEMBERSHIP_FOLLOW_UP_EMAIL",
        "MEMBERSHIP_OTP_LOGIN_EMAIL",
        "MEMBERSHIP_PASSWORD_RESET_EMAIL",
        "MEMBERSHIP_PASSWORD_SAVED_EMAIL",
        "MEMBERSHIP_PASSWORDLESS_AUTH_EMAIL",
        "MEMBERSHIP_REGISTRATION_EMAIL",
        "MEMBERSHIP_REGISTRATION_FOLLOW_UP_EMAIL",
        "MEMBERSHIP_VERIFICATION_EMAIL",
        "OPTIN_EMAIL",
        "OPTIN_FOLLOWUP_EMAIL",
        "RESUBSCRIBE_EMAIL",
        "RSS_EMAIL",
        "RSS_EMAIL_CHILD",
        "SINGLE_SEND_API",
        "SMTP_TOKEN",
        "TICKET_EMAIL",
    ]

    updated_after: Annotated[Union[str, datetime], PropertyInfo(alias="updatedAfter", format="iso8601")]

    updated_at: Annotated[Union[str, datetime], PropertyInfo(alias="updatedAt", format="iso8601")]

    updated_before: Annotated[Union[str, datetime], PropertyInfo(alias="updatedBefore", format="iso8601")]

    variant_stats: Annotated[bool, PropertyInfo(alias="variantStats")]

    workflow_names: Annotated[bool, PropertyInfo(alias="workflowNames")]
