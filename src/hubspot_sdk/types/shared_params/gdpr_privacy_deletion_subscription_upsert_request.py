# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["GdprPrivacyDeletionSubscriptionUpsertRequest"]


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
