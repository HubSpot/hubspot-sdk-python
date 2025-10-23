# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["SubscriptionCreateParams"]


class SubscriptionCreateParams(TypedDict, total=False):
    event_type: Required[
        Annotated[
            Literal[
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
            ],
            PropertyInfo(alias="eventType"),
        ]
    ]
    """Type of event to listen for.

    Can be one of `create`, `delete`, `deletedForPrivacy`, or `propertyChange`.
    """

    active: bool
    """Determines if the subscription is active or paused. Defaults to false."""

    object_type_id: Annotated[str, PropertyInfo(alias="objectTypeId")]

    property_name: Annotated[str, PropertyInfo(alias="propertyName")]
    """The internal name of the property to monitor for changes.

    Only applies when `eventType` is `propertyChange`.
    """
