# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["AppWebhookCreateSubscriptionParams"]


class AppWebhookCreateSubscriptionParams(TypedDict, total=False):
    active: Required[bool]
    """Determines if the subscription is active or paused. Defaults to false."""

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
    """Type of event to listen for.

    Can be one of `create`, `delete`, `deletedForPrivacy`, or `propertyChange`.
    """

    event_type_name: Annotated[str, PropertyInfo(alias="eventTypeName")]

    object_type_id: Annotated[str, PropertyInfo(alias="objectTypeId")]

    property_name: Annotated[str, PropertyInfo(alias="propertyName")]
    """The internal name of the property to monitor for changes.

    Only applies when `eventType` is `propertyChange`.
    """
