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
    """The unique ID of the webhook subscription."""

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
        ]
    ]

    app_id: int = FieldInfo(alias="appId")

    created_at: datetime = FieldInfo(alias="createdAt")
    """
    The timestamp when the webhook subscription was created, in ISO 8601 format
    (e.g., 2020-02-29T12:30:00Z).
    """

    object_type_id: str = FieldInfo(alias="objectTypeId")
    """The ID of the object type for the subscription.

    This can be a standard CRM object (e.g., 'contact', 'company', 'deal') or a
    custom object ID for custom object subscriptions.
    """

    subscription_type: Literal["APP_LIFECYCLE_EVENT", "ASSOCIATION", "EVENT", "LIST_MEMBERSHIP", "OBJECT"] = FieldInfo(
        alias="subscriptionType"
    )

    updated_at: datetime = FieldInfo(alias="updatedAt")
    """
    The timestamp when the webhook subscription was last updated, in ISO 8601 format
    (e.g., 2020-02-29T12:30:00Z).
    """

    action_overrides: Optional[Dict[str, ActionOverrideRequest]] = FieldInfo(alias="actionOverrides", default=None)

    associated_object_type_ids: Optional[List[str]] = FieldInfo(alias="associatedObjectTypeIds", default=None)

    created_by: Optional[int] = FieldInfo(alias="createdBy", default=None)

    deleted_at: Optional[datetime] = FieldInfo(alias="deletedAt", default=None)

    list_ids: Optional[List[int]] = FieldInfo(alias="listIds", default=None)

    object_ids: Optional[List[int]] = FieldInfo(alias="objectIds", default=None)

    portal_id: Optional[int] = FieldInfo(alias="portalId", default=None)

    properties: Optional[List[str]] = None
