# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo
from .public_delivery_identifier_param import PublicDeliveryIdentifierParam

__all__ = ["ChannelIntegrationParticipantParam"]


class ChannelIntegrationParticipantParam(TypedDict, total=False):
    delivery_identifier: Required[Annotated[PublicDeliveryIdentifierParam, PropertyInfo(alias="deliveryIdentifier")]]

    name: str
