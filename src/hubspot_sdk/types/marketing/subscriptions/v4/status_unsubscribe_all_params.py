# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ....._utils import PropertyInfo

__all__ = ["StatusUnsubscribeAllParams"]


class StatusUnsubscribeAllParams(TypedDict, total=False):
    channel: Required[Literal["EMAIL"]]
    """The channel type for the subscription type.

    Currently, the only supported channel type is `EMAIL`.
    """

    business_unit_id: Annotated[int, PropertyInfo(alias="businessUnitId")]
    """
    If you have the
    [business unit add-on](https://developers.hubspot.com/beta-docs/guides/api/settings/business-units-api),
    include this parameter to filter results by business unit ID. The default
    Account business unit will always use `0`.
    """

    verbose: bool
    """
    Set to `true` to include the details of the updated subscription statuses in the
    response. Not including this parameter will result in an empty response.
    """
