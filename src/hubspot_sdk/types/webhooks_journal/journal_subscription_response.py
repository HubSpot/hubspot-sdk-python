# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from ..shared.action_override_request import ActionOverrideRequest

__all__ = ["JournalSubscriptionResponse"]


class JournalSubscriptionResponse(BaseModel):
    id: int
    """The unique identifier for the subscription, represented as an integer."""

    actions: List[
        Literal[
            "CREATE",
            "UPDATE",
            "DELETE",
            "MERGE",
            "RESTORE",
            "ASSOCIATION_ADDED",
            "ASSOCIATION_REMOVED",
            "SNAPSHOT",
            "APP_INSTALL",
            "APP_UNINSTALL",
            "ADDED_TO_LIST",
            "REMOVED_FROM_LIST",
            "GDPR_DELETE",
        ]
    ]
    """An array of actions associated with the subscription.

    Valid actions include 'CREATE', 'UPDATE', 'DELETE', 'MERGE', 'RESTORE',
    'ASSOCIATION_ADDED', 'ASSOCIATION_REMOVED', 'SNAPSHOT', 'APP_INSTALL',
    'APP_UNINSTALL', 'ADDED_TO_LIST', 'REMOVED_FROM_LIST', and 'GDPR_DELETE'.
    """

    app_id: int = FieldInfo(alias="appId")
    """
    The unique identifier for the app associated with the subscription, represented
    as an integer.
    """

    created_at: datetime = FieldInfo(alias="createdAt")
    """The date and time when the subscription was created, in ISO 8601 format."""

    object_type_id: str = FieldInfo(alias="objectTypeId")
    """
    The identifier for the type of object associated with the subscription,
    represented as a string.
    """

    subscription_type: Literal[
        "APP_LIFECYCLE_EVENT", "ASSOCIATION", "EVENT", "GDPR_PRIVACY_DELETION", "LIST_MEMBERSHIP", "OBJECT"
    ] = FieldInfo(alias="subscriptionType")
    """The type of subscription, indicating the nature of events it pertains to.

    Valid values include 'OBJECT', 'ASSOCIATION', 'EVENT', 'APP_LIFECYCLE_EVENT',
    'LIST_MEMBERSHIP', and 'GDPR_PRIVACY_DELETION'.
    """

    updated_at: datetime = FieldInfo(alias="updatedAt")
    """The date and time when the subscription was last updated, in ISO 8601 format."""

    action_overrides: Optional[Dict[str, ActionOverrideRequest]] = FieldInfo(alias="actionOverrides", default=None)
    """
    An object containing overrides for actions, where each key is an action and the
    value is an ActionOverrideRequest object.
    """

    associated_object_type_ids: Optional[List[str]] = FieldInfo(alias="associatedObjectTypeIds", default=None)
    """An array of strings representing the IDs of associated object types."""

    created_by: Optional[int] = FieldInfo(alias="createdBy", default=None)
    """
    The unique identifier of the user who created the subscription, represented as
    an integer.
    """

    deleted_at: Optional[datetime] = FieldInfo(alias="deletedAt", default=None)
    """
    The date and time when the subscription was deleted, in ISO 8601 format, if
    applicable.
    """

    list_ids: Optional[List[int]] = FieldInfo(alias="listIds", default=None)
    """
    An array of integers representing the IDs of lists associated with the
    subscription.
    """

    object_ids: Optional[List[int]] = FieldInfo(alias="objectIds", default=None)
    """
    An array of integers representing the IDs of objects associated with the
    subscription.
    """

    portal_id: Optional[int] = FieldInfo(alias="portalId", default=None)
    """
    The unique identifier for the portal associated with the subscription,
    represented as an integer.
    """

    properties: Optional[List[str]] = None
    """
    An array of strings representing the properties associated with the
    subscription.
    """
