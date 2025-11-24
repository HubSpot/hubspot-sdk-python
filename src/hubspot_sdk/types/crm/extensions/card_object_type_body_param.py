# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ...._types import SequenceNotStr
from ...._utils import PropertyInfo

__all__ = ["CardObjectTypeBodyParam"]


class CardObjectTypeBodyParam(TypedDict, total=False):
    name: Required[Literal["companies", "contacts", "deals", "marketing_events", "tickets"]]
    """A CRM object type where this card should be displayed."""

    properties_to_send: Required[Annotated[SequenceNotStr[str], PropertyInfo(alias="propertiesToSend")]]
    """
    An array of properties that should be sent to this card's target URL when the
    data fetch request is made. Must be valid properties for the corresponding CRM
    object type.
    """
