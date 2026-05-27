# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["ListMembershipSubscriptionUpsertRequest"]


class ListMembershipSubscriptionUpsertRequest(BaseModel):
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

    list_ids: List[int] = FieldInfo(alias="listIds")

    object_ids: List[int] = FieldInfo(alias="objectIds")

    portal_id: int = FieldInfo(alias="portalId")

    subscription_type: Literal["LIST_MEMBERSHIP"] = FieldInfo(alias="subscriptionType")
