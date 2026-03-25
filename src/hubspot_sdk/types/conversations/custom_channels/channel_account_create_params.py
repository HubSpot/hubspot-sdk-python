# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ...._utils import PropertyInfo
from ..public_delivery_identifier_param import PublicDeliveryIdentifierParam

__all__ = ["ChannelAccountCreateParams"]


class ChannelAccountCreateParams(TypedDict, total=False):
    authorized: Required[bool]

    inbox_id: Required[Annotated[str, PropertyInfo(alias="inboxId")]]

    name: Required[str]

    delivery_identifier: Annotated[PublicDeliveryIdentifierParam, PropertyInfo(alias="deliveryIdentifier")]
