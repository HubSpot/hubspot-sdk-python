# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .action_override_request import ActionOverrideRequest

__all__ = ["SubscriptionResponse1"]


class SubscriptionResponse1(BaseModel):
    id: int
    """The unique identifier for the subscription.

    It is an integer formatted as int64.
    """

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
    """A list of actions that trigger the subscription.

    Possible values include 'CREATE', 'UPDATE', 'DELETE', 'MERGE', 'RESTORE',
    'ASSOCIATION_ADDED', 'ASSOCIATION_REMOVED', 'SNAPSHOT', 'APP_INSTALL',
    'APP_UNINSTALL', 'ADDED_TO_LIST', 'REMOVED_FROM_LIST', and 'GDPR_DELETE'.
    """

    app_id: int = FieldInfo(alias="appId")
    """The unique identifier for the app associated with the subscription.

    It is an integer formatted as int64.
    """

    created_at: datetime = FieldInfo(alias="createdAt")
    """The date and time when the subscription was created, in ISO 8601 format."""

    object_type_id: str = FieldInfo(alias="objectTypeId")
    """The identifier for the object type associated with the subscription.

    It is a string.
    """

    subscription_type: Literal[
        "APP_LIFECYCLE_EVENT", "ASSOCIATION", "EVENT", "GDPR_PRIVACY_DELETION", "LIST_MEMBERSHIP", "OBJECT"
    ] = FieldInfo(alias="subscriptionType")
    """
    The type of subscription, which can be one of the following: 'OBJECT',
    'ASSOCIATION', 'EVENT', 'APP_LIFECYCLE_EVENT', 'LIST_MEMBERSHIP', or
    'GDPR_PRIVACY_DELETION'.
    """

    updated_at: datetime = FieldInfo(alias="updatedAt")
    """The date and time when the subscription was last updated, in ISO 8601 format."""

    action_overrides: Optional[Dict[str, ActionOverrideRequest]] = FieldInfo(alias="actionOverrides", default=None)
    """
    An object containing action overrides, where each key is an action and the value
    is an ActionOverrideRequest object.
    """

    associated_object_type_ids: Optional[List[str]] = FieldInfo(alias="associatedObjectTypeIds", default=None)
    """A list of associated object type IDs. Each ID is a string."""

    created_by: Optional[int] = FieldInfo(alias="createdBy", default=None)
    """The ID of the user who created the subscription.

    It is an integer formatted as int64.
    """

    deleted_at: Optional[datetime] = FieldInfo(alias="deletedAt", default=None)
    """
    The date and time when the subscription was deleted, in ISO 8601 format, if
    applicable.
    """

    list_ids: Optional[List[int]] = FieldInfo(alias="listIds", default=None)
    """A list of list IDs associated with the subscription.

    Each ID is an integer formatted as int64.
    """

    object_ids: Optional[List[int]] = FieldInfo(alias="objectIds", default=None)
    """A list of object IDs associated with the subscription.

    Each ID is an integer formatted as int64.
    """

    portal_id: Optional[int] = FieldInfo(alias="portalId", default=None)
    """The unique identifier for the portal associated with the subscription.

    It is an integer formatted as int64.
    """

    properties: Optional[List[str]] = None
    """A list of property names associated with the subscription.

    Each property is a string.
    """
