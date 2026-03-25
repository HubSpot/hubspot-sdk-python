# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["MessageUpdateParams"]


class MessageUpdateParams(TypedDict, total=False):
    channel_id: Required[Annotated[int, PropertyInfo(alias="channelId")]]

    status_type: Required[Annotated[Literal["FAILED", "READ", "SENT"], PropertyInfo(alias="statusType")]]
    """Valid status are SENT, FAILED, and READ"""

    error_message: Annotated[str, PropertyInfo(alias="errorMessage")]
