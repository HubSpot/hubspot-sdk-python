# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .public_delivery_identifier import PublicDeliveryIdentifier

__all__ = ["PublicSender"]


class PublicSender(BaseModel):
    actor_id: Optional[str] = FieldInfo(alias="actorId", default=None)

    delivery_identifier: Optional[PublicDeliveryIdentifier] = FieldInfo(alias="deliveryIdentifier", default=None)

    name: Optional[str] = None

    sender_field: Optional[str] = FieldInfo(alias="senderField", default=None)
