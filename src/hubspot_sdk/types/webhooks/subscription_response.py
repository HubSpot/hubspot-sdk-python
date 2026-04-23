# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["SubscriptionResponse"]


class SubscriptionResponse(BaseModel):
    id: str
    """The unique identifier for the subscription.

    It is an integer formatted as int64.
    """

    active: bool
    """A boolean indicating whether the subscription is currently active."""

    created_at: datetime = FieldInfo(alias="createdAt")
    """The date and time when the subscription was created, in ISO 8601 format."""

    event_type: Literal[
        "company.associationChange",
        "company.creation",
        "company.deletion",
        "company.merge",
        "company.propertyChange",
        "company.restore",
        "contact.associationChange",
        "contact.creation",
        "contact.deletion",
        "contact.merge",
        "contact.privacyDeletion",
        "contact.propertyChange",
        "contact.restore",
        "conversation.creation",
        "conversation.deletion",
        "conversation.newMessage",
        "conversation.privacyDeletion",
        "conversation.propertyChange",
        "deal.associationChange",
        "deal.creation",
        "deal.deletion",
        "deal.merge",
        "deal.propertyChange",
        "deal.restore",
        "event.completed",
        "line_item.associationChange",
        "line_item.creation",
        "line_item.deletion",
        "line_item.merge",
        "line_item.propertyChange",
        "line_item.restore",
        "object.associationChange",
        "object.creation",
        "object.deletion",
        "object.merge",
        "object.propertyChange",
        "object.restore",
        "product.creation",
        "product.deletion",
        "product.merge",
        "product.propertyChange",
        "product.restore",
        "ticket.associationChange",
        "ticket.creation",
        "ticket.deletion",
        "ticket.merge",
        "ticket.propertyChange",
        "ticket.restore",
    ] = FieldInfo(alias="eventType")
    """The type of event that triggers the subscription.

    Valid values include various property changes, creations, deletions, merges,
    restores, and association changes for different HubSpot objects.
    """

    event_type_name: Optional[str] = FieldInfo(alias="eventTypeName", default=None)
    """The name of the event type for the subscription."""

    object_type_id: Optional[str] = FieldInfo(alias="objectTypeId", default=None)
    """The identifier for the object type associated with the subscription.

    It is a string.
    """

    property_name: Optional[str] = FieldInfo(alias="propertyName", default=None)
    """The name of the property associated with the subscription event, if applicable."""

    updated_at: Optional[datetime] = FieldInfo(alias="updatedAt", default=None)
    """The date and time when the subscription was last updated, in ISO 8601 format."""
