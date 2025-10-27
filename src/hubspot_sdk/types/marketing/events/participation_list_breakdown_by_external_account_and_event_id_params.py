# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["ParticipationListBreakdownByExternalAccountAndEventIDParams"]


class ParticipationListBreakdownByExternalAccountAndEventIDParams(TypedDict, total=False):
    external_account_id: Required[Annotated[str, PropertyInfo(alias="externalAccountId")]]

    after: str
    """The cursor indicating the position of the last retrieved item."""

    contact_identifier: Annotated[str, PropertyInfo(alias="contactIdentifier")]
    """The identifier of the Contact. It may be email or internal id."""

    limit: int
    """The limit for response size. The default value is 10, the max number is 100"""

    state: str
    """The participation state value.

    It may be REGISTERED, CANCELLED, ATTENDED, NO_SHOW
    """
