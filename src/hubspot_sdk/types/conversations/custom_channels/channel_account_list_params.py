# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, Annotated, TypedDict

from ...._types import SequenceNotStr
from ...._utils import PropertyInfo

__all__ = ["ChannelAccountListParams"]


class ChannelAccountListParams(TypedDict, total=False):
    after: str
    """
    The paging cursor token of the last successfully read resource will be returned
    as the `paging.next.after` JSON property of a paged response containing more
    results.
    """

    archived: bool
    """Whether to return only results that have been archived."""

    default_page_length: Annotated[int, PropertyInfo(alias="defaultPageLength")]

    delivery_identifier_type: Annotated[
        List[Literal["HS_EMAIL_ADDRESS", "HS_PHONE_NUMBER", "HS_SHORT_CODE", "CHANNEL_SPECIFIC_OPAQUE_ID"]],
        PropertyInfo(alias="deliveryIdentifierType"),
    ]

    delivery_identifier_value: Annotated[SequenceNotStr[str], PropertyInfo(alias="deliveryIdentifierValue")]

    limit: int
    """The maximum number of results to display per page."""

    sort: SequenceNotStr[str]
