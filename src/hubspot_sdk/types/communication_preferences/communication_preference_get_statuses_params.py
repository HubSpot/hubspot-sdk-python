# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["CommunicationPreferenceGetStatusesParams"]


class CommunicationPreferenceGetStatusesParams(TypedDict, total=False):
    channel: Required[Literal["EMAIL"]]
    """
    A required string indicating the communication channel to retrieve the status
    for. Valid value is 'EMAIL'.
    """

    business_unit_id: Annotated[int, PropertyInfo(alias="businessUnitId")]
    """
    An optional integer representing the business unit ID to filter the subscription
    status.
    """
