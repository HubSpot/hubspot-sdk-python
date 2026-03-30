# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["SubscriptionResponse"]


class SubscriptionResponse(BaseModel):
    id: str
    """The unique ID of the webhook subscription."""

    active: bool
    """Whether the subscription is active or paused.

    If true, the subscription will send webhook notifications. If false, the
    subscription is paused and will not send notifications.
    """

    created_at: datetime = FieldInfo(alias="createdAt")
    """
    The timestamp when the webhook subscription was created, in ISO 8601 format
    (e.g., 2020-02-29T12:30:00Z).
    """

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
    """The type of event to listen for.

    Accepted values include contact.creation, contact.deletion,
    contact.propertyChange, and similar event types for other CRM objects and custom
    objects.
    """

    event_type_name: Optional[str] = FieldInfo(alias="eventTypeName", default=None)
    """The name of the event to listen for.

    This is used with custom objects to specify custom event types beyond the
    standard eventType enum values.
    """

    object_type_id: Optional[str] = FieldInfo(alias="objectTypeId", default=None)
    """The ID of the object type for the subscription.

    This can be a standard CRM object (e.g., 'contact', 'company', 'deal') or a
    custom object ID for custom object subscriptions.
    """

    property_name: Optional[str] = FieldInfo(alias="propertyName", default=None)
    """The internal name of the property to monitor for changes.

    Only applies when eventType is propertyChange.
    """

    updated_at: Optional[datetime] = FieldInfo(alias="updatedAt", default=None)
    """
    The timestamp when the webhook subscription was last updated, in ISO 8601 format
    (e.g., 2020-02-29T12:30:00Z).
    """
