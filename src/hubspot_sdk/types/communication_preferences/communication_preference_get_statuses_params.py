# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["CommunicationPreferenceGetStatusesParams"]


class CommunicationPreferenceGetStatusesParams(TypedDict, total=False):
    channel: Required[Literal["EMAIL"]]
    """The communication channel for which the subscription status is being retrieved.

    This parameter is required and currently supports only 'EMAIL'.
    """

    business_unit_id: Annotated[int, PropertyInfo(alias="businessUnitId")]
    """The ID of the business unit to filter the subscription status by.

    This is an optional parameter.
    """
