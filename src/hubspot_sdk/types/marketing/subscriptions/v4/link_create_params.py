# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ....._utils import PropertyInfo

__all__ = ["LinkCreateParams"]


class LinkCreateParams(TypedDict, total=False):
    channel: Required[Literal["EMAIL"]]

    subscriber_id_string: Required[Annotated[str, PropertyInfo(alias="subscriberIdString")]]

    business_unit_id: Annotated[int, PropertyInfo(alias="businessUnitId")]

    language: str

    subscription_id: Annotated[int, PropertyInfo(alias="subscriptionId")]
