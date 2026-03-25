# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["PublicDeliveryIdentifier"]


class PublicDeliveryIdentifier(BaseModel):
    type: Literal["CHANNEL_SPECIFIC_OPAQUE_ID", "HS_EMAIL_ADDRESS", "HS_PHONE_NUMBER", "HS_SHORT_CODE"]

    value: str
