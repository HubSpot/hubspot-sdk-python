# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["ListMembershipSubscriptionUpsertRequestParam"]


class ListMembershipSubscriptionUpsertRequestParam(TypedDict, total=False):
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
            ]
        ]
    ]

    list_ids: Required[Annotated[Iterable[int], PropertyInfo(alias="listIds")]]

    object_ids: Required[Annotated[Iterable[int], PropertyInfo(alias="objectIds")]]

    portal_id: Required[Annotated[int, PropertyInfo(alias="portalId")]]

    subscription_type: Required[
        Annotated[
            Literal["OBJECT", "ASSOCIATION", "EVENT", "APP_LIFECYCLE_EVENT", "LIST_MEMBERSHIP"],
            PropertyInfo(alias="subscriptionType"),
        ]
    ]
