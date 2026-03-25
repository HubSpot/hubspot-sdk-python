# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["PublicDeliveryIdentifierParam"]


class PublicDeliveryIdentifierParam(TypedDict, total=False):
    type: Required[Literal["CHANNEL_SPECIFIC_OPAQUE_ID", "HS_EMAIL_ADDRESS", "HS_PHONE_NUMBER", "HS_SHORT_CODE"]]

    value: Required[str]
