# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import TypeAlias

from .object_subscription_upsert_request import ObjectSubscriptionUpsertRequest
from .association_subscription_upsert_request import AssociationSubscriptionUpsertRequest
from .list_membership_subscription_upsert_request import ListMembershipSubscriptionUpsertRequest
from .app_lifecycle_event_subscription_upsert_request import AppLifecycleEventSubscriptionUpsertRequest
from .gdpr_privacy_deletion_subscription_upsert_request import GdprPrivacyDeletionSubscriptionUpsertRequest

__all__ = ["SubscriptionUpsertRequest"]

SubscriptionUpsertRequest: TypeAlias = Union[
    ObjectSubscriptionUpsertRequest,
    AssociationSubscriptionUpsertRequest,
    AppLifecycleEventSubscriptionUpsertRequest,
    ListMembershipSubscriptionUpsertRequest,
    GdprPrivacyDeletionSubscriptionUpsertRequest,
]
