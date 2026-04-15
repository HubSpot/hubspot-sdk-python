# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["WebhookCreateEventSubscriptionParams"]


class WebhookCreateEventSubscriptionParams(TypedDict, total=False):
    active: Required[bool]
    """A boolean indicating whether the subscription is active.

    This field is required.
    """

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

    Valid values include various object changes such as 'contact.propertyChange',
    'deal.creation', and 'conversation.newMessage'.
    """

    event_type_name: Annotated[str, PropertyInfo(alias="eventTypeName")]
    """A string that provides a human-readable name for the event type.

    This is optional.
    """

    object_type_id: Annotated[str, PropertyInfo(alias="objectTypeId")]
    """
    A string representing the identifier of the object type for which the
    subscription is being created. This is optional.
    """

    property_name: Annotated[str, PropertyInfo(alias="propertyName")]
    """A string indicating the name of the property that triggers the event.

    This is optional and used when subscribing to property change events.
    """
