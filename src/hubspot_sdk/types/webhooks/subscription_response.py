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
