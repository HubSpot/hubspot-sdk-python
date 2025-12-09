# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import datetime
from typing_extensions import TypeAlias

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .public_list_permissions import PublicListPermissions
from .public_membership_settings import PublicMembershipSettings

__all__ = ["PublicObjectList", "FilterBranch"]

FilterBranch: TypeAlias = Union[
    "PublicOrFilterBranch",
    "PublicAndFilterBranch",
    "PublicNotAllFilterBranch",
    "PublicNotAnyFilterBranch",
    "PublicRestrictedFilterBranch",
    "PublicUnifiedEventsFilterBranch",
    "PublicPropertyAssociationFilterBranch",
    "PublicAssociationFilterBranch",
]


class PublicObjectList(BaseModel):
    """An object list definition."""

    list_id: str = FieldInfo(alias="listId")
    """The **ILS ID** of the list."""

    list_version: int = FieldInfo(alias="listVersion")
    """The version of the list."""

    name: str
    """The name of the list."""

    object_type_id: str = FieldInfo(alias="objectTypeId")
    """The object type of the list."""

    processing_status: str = FieldInfo(alias="processingStatus")
    """The processing status of the list."""

    processing_type: str = FieldInfo(alias="processingType")
    """The processing type of the list."""

    created_at: Optional[datetime] = FieldInfo(alias="createdAt", default=None)
    """The time when the list was created."""

    created_by_id: Optional[str] = FieldInfo(alias="createdById", default=None)
    """The ID of the user that created the list."""

    deleted_at: Optional[datetime] = FieldInfo(alias="deletedAt", default=None)
    """The time when the list was deleted."""

    filter_branch: Optional[FilterBranch] = FieldInfo(alias="filterBranch", default=None)

    filters_updated_at: Optional[datetime] = FieldInfo(alias="filtersUpdatedAt", default=None)
    """The time when the filters for this list were last updated."""

    list_permissions: Optional[PublicListPermissions] = FieldInfo(alias="listPermissions", default=None)

    membership_settings: Optional[PublicMembershipSettings] = FieldInfo(alias="membershipSettings", default=None)

    size: Optional[int] = None
    """Size of the list"""

    updated_at: Optional[datetime] = FieldInfo(alias="updatedAt", default=None)
    """The time the list was last updated."""

    updated_by_id: Optional[str] = FieldInfo(alias="updatedById", default=None)
    """The ID of the user that last updated the list."""


from ..shared.public_or_filter_branch import PublicOrFilterBranch
from ..shared.public_and_filter_branch import PublicAndFilterBranch
from ..shared.public_not_all_filter_branch import PublicNotAllFilterBranch
from ..shared.public_not_any_filter_branch import PublicNotAnyFilterBranch
from ..shared.public_restricted_filter_branch import PublicRestrictedFilterBranch
from ..shared.public_association_filter_branch import PublicAssociationFilterBranch
from ..shared.public_unified_events_filter_branch import PublicUnifiedEventsFilterBranch
from ..shared.public_property_association_filter_branch import PublicPropertyAssociationFilterBranch
