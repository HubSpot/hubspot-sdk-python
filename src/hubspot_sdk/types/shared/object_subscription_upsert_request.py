# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["ObjectSubscriptionUpsertRequest"]


class ObjectSubscriptionUpsertRequest(BaseModel):
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

    object_ids: List[int] = FieldInfo(alias="objectIds")

    object_type_id: str = FieldInfo(alias="objectTypeId")

    portal_id: int = FieldInfo(alias="portalId")

    properties: List[str]

    subscription_type: Literal["OBJECT"] = FieldInfo(alias="subscriptionType")
