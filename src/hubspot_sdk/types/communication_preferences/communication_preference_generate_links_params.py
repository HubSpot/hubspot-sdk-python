# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["CommunicationPreferenceGenerateLinksParams"]


class CommunicationPreferenceGenerateLinksParams(TypedDict, total=False):
    channel: Required[Literal["EMAIL"]]
    """The communication channel for which the links are generated. Must be 'EMAIL'."""

    subscriber_id_string: Required[Annotated[str, PropertyInfo(alias="subscriberIdString")]]
    """A string representing the unique identifier of the subscriber.

    This property is required.
    """

    business_unit_id: Annotated[int, PropertyInfo(alias="businessUnitId")]
    """The ID of the business unit associated with the request. Defaults to 0."""

    language: str
    """
    The language in which the generated link should be presented, represented as a
    string.
    """

    subscription_id: Annotated[int, PropertyInfo(alias="subscriptionId")]
    """
    The unique identifier for the subscription, represented as an integer in int64
    format.
    """
