# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo

__all__ = ["ObjectSubscriptionUpsertRequestParam"]


class ObjectSubscriptionUpsertRequestParam(TypedDict, total=False):
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

    object_ids: Required[Annotated[Iterable[int], PropertyInfo(alias="objectIds")]]

    object_type_id: Required[Annotated[str, PropertyInfo(alias="objectTypeId")]]

    portal_id: Required[Annotated[int, PropertyInfo(alias="portalId")]]

    properties: Required[SequenceNotStr[str]]

    subscription_type: Required[
        Annotated[
            Literal["OBJECT", "ASSOCIATION", "EVENT", "APP_LIFECYCLE_EVENT", "LIST_MEMBERSHIP"],
            PropertyInfo(alias="subscriptionType"),
        ]
    ]
