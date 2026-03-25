# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["CommunicationPreferenceUnsubscribeAllParams"]


class CommunicationPreferenceUnsubscribeAllParams(TypedDict, total=False):
    channel: Required[Literal["EMAIL"]]
    """The communication channel from which to unsubscribe the subscriber.

    Must be 'EMAIL'.
    """

    business_unit_id: Annotated[int, PropertyInfo(alias="businessUnitId")]
    """The ID of the business unit associated with the subscriber.

    This is an optional parameter.
    """

    verbose: bool
    """
    A boolean flag indicating whether to include detailed information in the
    response. Defaults to false.
    """
