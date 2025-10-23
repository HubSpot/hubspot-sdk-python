# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["SubscriptionResponse"]


class SubscriptionResponse(BaseModel):
    id: str
    """The unique ID of the subscription."""

    active: bool
    """Determines if the subscription is active or paused."""

    created_at: datetime = FieldInfo(alias="createdAt")
    """When this subscription was created.

    Formatted as milliseconds from the [Unix epoch](#).
    """

    event_type: Literal[
        "contact.propertyChange",
        "company.propertyChange",
        "deal.propertyChange",
        "ticket.propertyChange",
        "product.propertyChange",
        "line_item.propertyChange",
        "contact.creation",
        "contact.deletion",
        "contact.privacyDeletion",
        "company.creation",
        "company.deletion",
        "deal.creation",
        "deal.deletion",
        "ticket.creation",
        "ticket.deletion",
        "product.creation",
        "product.deletion",
        "line_item.creation",
        "line_item.deletion",
        "conversation.creation",
        "conversation.deletion",
        "conversation.newMessage",
        "conversation.privacyDeletion",
        "conversation.propertyChange",
        "contact.merge",
        "company.merge",
        "deal.merge",
        "ticket.merge",
        "product.merge",
        "line_item.merge",
        "contact.restore",
        "company.restore",
        "deal.restore",
        "ticket.restore",
        "product.restore",
        "line_item.restore",
        "contact.associationChange",
        "company.associationChange",
        "deal.associationChange",
        "ticket.associationChange",
        "line_item.associationChange",
        "object.propertyChange",
        "object.creation",
        "object.deletion",
        "object.merge",
        "object.restore",
        "object.associationChange",
    ] = FieldInfo(alias="eventType")
    """Type of event to listen for.

    Can be one of `create`, `delete`, `deletedForPrivacy`, or `propertyChange`.
    """

    object_type_id: Optional[str] = FieldInfo(alias="objectTypeId", default=None)
    """The identifier of the object type associated with the subscription."""

    property_name: Optional[str] = FieldInfo(alias="propertyName", default=None)
    """The internal name of the property being monitored for changes.

    Only applies when `eventType` is `propertyChange`.
    """

    updated_at: Optional[datetime] = FieldInfo(alias="updatedAt", default=None)
    """When this subscription was last updated.

    Formatted as milliseconds from the [Unix epoch](#).
    """
