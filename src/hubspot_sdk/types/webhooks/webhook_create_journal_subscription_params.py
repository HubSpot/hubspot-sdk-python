# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo

__all__ = [
    "WebhookCreateJournalSubscriptionParams",
    "ObjectSubscriptionUpsertRequest",
    "AssociationSubscriptionUpsertRequest",
    "AppLifecycleEventSubscriptionUpsertRequest",
    "ListMembershipSubscriptionUpsertRequest",
    "GdprPrivacyDeletionSubscriptionUpsertRequest",
]


class ObjectSubscriptionUpsertRequest(TypedDict, total=False):
    actions: Required[
        List[
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
    ]

    object_ids: Required[Annotated[Iterable[int], PropertyInfo(alias="objectIds")]]

    object_type_id: Required[Annotated[str, PropertyInfo(alias="objectTypeId")]]

    portal_id: Required[Annotated[int, PropertyInfo(alias="portalId")]]

    properties: Required[SequenceNotStr[str]]

    subscription_type: Required[Annotated[Literal["OBJECT"], PropertyInfo(alias="subscriptionType")]]


class AssociationSubscriptionUpsertRequest(TypedDict, total=False):
    actions: Required[
        List[
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
    ]

    associated_object_type_ids: Required[Annotated[SequenceNotStr[str], PropertyInfo(alias="associatedObjectTypeIds")]]

    object_ids: Required[Annotated[Iterable[int], PropertyInfo(alias="objectIds")]]

    object_type_id: Required[Annotated[str, PropertyInfo(alias="objectTypeId")]]

    portal_id: Required[Annotated[int, PropertyInfo(alias="portalId")]]

    subscription_type: Required[Annotated[Literal["ASSOCIATION"], PropertyInfo(alias="subscriptionType")]]


class AppLifecycleEventSubscriptionUpsertRequest(TypedDict, total=False):
    event_type_id: Required[Annotated[str, PropertyInfo(alias="eventTypeId")]]

    properties: Required[SequenceNotStr[str]]

    subscription_type: Required[Annotated[Literal["APP_LIFECYCLE_EVENT"], PropertyInfo(alias="subscriptionType")]]


class ListMembershipSubscriptionUpsertRequest(TypedDict, total=False):
    actions: Required[
        List[
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
    ]

    list_ids: Required[Annotated[Iterable[int], PropertyInfo(alias="listIds")]]

    object_ids: Required[Annotated[Iterable[int], PropertyInfo(alias="objectIds")]]

    portal_id: Required[Annotated[int, PropertyInfo(alias="portalId")]]

    subscription_type: Required[Annotated[Literal["LIST_MEMBERSHIP"], PropertyInfo(alias="subscriptionType")]]


class GdprPrivacyDeletionSubscriptionUpsertRequest(TypedDict, total=False):
    actions: Required[
        List[
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
    ]

    object_type_id: Required[Annotated[str, PropertyInfo(alias="objectTypeId")]]

    portal_id: Required[Annotated[int, PropertyInfo(alias="portalId")]]

    subscription_type: Required[Annotated[Literal["GDPR_PRIVACY_DELETION"], PropertyInfo(alias="subscriptionType")]]


WebhookCreateJournalSubscriptionParams: TypeAlias = Union[
    ObjectSubscriptionUpsertRequest,
    AssociationSubscriptionUpsertRequest,
    AppLifecycleEventSubscriptionUpsertRequest,
    ListMembershipSubscriptionUpsertRequest,
    GdprPrivacyDeletionSubscriptionUpsertRequest,
]
