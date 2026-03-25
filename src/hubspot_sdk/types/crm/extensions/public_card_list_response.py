# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ...._models import BaseModel
from .public_card_response import PublicCardResponse

__all__ = ["PublicCardListResponse"]


class PublicCardListResponse(BaseModel):
    results: List[PublicCardResponse]
    """A list of card responses"""
