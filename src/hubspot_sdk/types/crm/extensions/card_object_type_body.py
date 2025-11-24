# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["CardObjectTypeBody"]


class CardObjectTypeBody(BaseModel):
    name: Literal["companies", "contacts", "deals", "marketing_events", "tickets"]
    """A CRM object type where this card should be displayed."""

    properties_to_send: List[str] = FieldInfo(alias="propertiesToSend")
    """
    An array of properties that should be sent to this card's target URL when the
    data fetch request is made. Must be valid properties for the corresponding CRM
    object type.
    """
