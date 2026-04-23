# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["WebhookCreateEventSubscriptionParams"]


class WebhookCreateEventSubscriptionParams(TypedDict, total=False):
    active: Required[bool]
    """A boolean indicating whether the subscription is active."""

    event_type: Required[
        Annotated[
            Literal[
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
            ],
            PropertyInfo(alias="eventType"),
        ]
    ]
    """A string representing the type of event to subscribe to.

    Valid values include various property changes, creations, deletions, merges,
    restorations, association changes, and event completions.
    """

    event_type_name: Annotated[str, PropertyInfo(alias="eventTypeName")]
    """A string providing a human-readable name for the event type."""

    object_type_id: Annotated[str, PropertyInfo(alias="objectTypeId")]
    """
    A string representing the ID of the object type associated with the
    subscription.
    """

    property_name: Annotated[str, PropertyInfo(alias="propertyName")]
    """
    A string indicating the specific property name related to the event type, if
    applicable.
    """
