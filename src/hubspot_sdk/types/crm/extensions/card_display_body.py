# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ...._models import BaseModel
from .card_display_property import CardDisplayProperty

__all__ = ["CardDisplayBody"]


class CardDisplayBody(BaseModel):
    """Configuration for displayed info on a card"""

    properties: List[CardDisplayProperty]
    """Card display properties.

    These will will be rendered as "label : value" pairs in the card UI. See the
    [example card](#) in the overview docs for more details.
    """
