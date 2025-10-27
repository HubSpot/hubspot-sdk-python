# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo
from .public_delivery_identifier_param import PublicDeliveryIdentifierParam

__all__ = ["PublicRecipientEggParam"]


class PublicRecipientEggParam(TypedDict, total=False):
    delivery_identifiers: Required[
        Annotated[Iterable[PublicDeliveryIdentifierParam], PropertyInfo(alias="deliveryIdentifiers")]
    ]

    actor_id: Annotated[str, PropertyInfo(alias="actorId")]

    delivery_identifier: Annotated[PublicDeliveryIdentifierParam, PropertyInfo(alias="deliveryIdentifier")]

    name: str

    recipient_field: Annotated[str, PropertyInfo(alias="recipientField")]
