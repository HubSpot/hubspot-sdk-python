# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .public_delivery_identifier import PublicDeliveryIdentifier

__all__ = ["PublicRecipient"]


class PublicRecipient(BaseModel):
    delivery_identifier: PublicDeliveryIdentifier = FieldInfo(alias="deliveryIdentifier")

    actor_id: Optional[str] = FieldInfo(alias="actorId", default=None)

    name: Optional[str] = None

    recipient_field: Optional[str] = FieldInfo(alias="recipientField", default=None)
