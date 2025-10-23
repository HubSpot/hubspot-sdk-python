# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

from .card_display_property_param import CardDisplayPropertyParam

__all__ = ["CardDisplayBodyParam"]


class CardDisplayBodyParam(TypedDict, total=False):
    properties: Required[Iterable[CardDisplayPropertyParam]]
    """Card display properties.

    These will will be rendered as "label : value" pairs in the card UI. See the
    [example card](#) in the overview docs for more details.
    """
