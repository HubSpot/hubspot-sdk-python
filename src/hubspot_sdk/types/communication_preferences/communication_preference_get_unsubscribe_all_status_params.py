# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["CommunicationPreferenceGetUnsubscribeAllStatusParams"]


class CommunicationPreferenceGetUnsubscribeAllStatusParams(TypedDict, total=False):
    channel: Required[Literal["EMAIL"]]
    """The communication channel from which to unsubscribe the subscriber.

    This is a required parameter and must be 'EMAIL'.
    """

    business_unit_id: Annotated[int, PropertyInfo(alias="businessUnitId")]
    """The ID of the business unit to which the subscriber belongs.

    This is an optional parameter.
    """

    verbose: bool
    """A boolean indicating whether to include detailed information in the response.

    Defaults to false.
    """
