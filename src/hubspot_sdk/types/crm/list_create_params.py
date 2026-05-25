# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union
from typing_extensions import Required, Annotated, TypeAlias, TypedDict

from ..._utils import PropertyInfo
from .public_list_permissions_param import PublicListPermissionsParam
from .public_membership_settings_param import PublicMembershipSettingsParam

__all__ = ["ListCreateParams", "FilterBranch"]


class ListCreateParams(TypedDict, total=False):
    name: Required[str]
    """
    The name of the list, which must be globally unique across all public lists in
    the portal.
    """

    object_type_id: Required[Annotated[str, PropertyInfo(alias="objectTypeId")]]
    """The object type ID of the type of objects that the list will store."""

    processing_type: Required[Annotated[str, PropertyInfo(alias="processingType")]]
    """The processing type of the list. One of: `SNAPSHOT`, `MANUAL`, or `DYNAMIC`."""

    custom_properties: Annotated[Dict[str, str], PropertyInfo(alias="customProperties")]
    """The list of custom properties to tie to the list.

    Custom property name is the key, the value is the value.
    """

    filter_branch: Annotated[FilterBranch, PropertyInfo(alias="filterBranch")]
    """Filter branch object containing filtering criteria for the list"""

    list_folder_id: Annotated[int, PropertyInfo(alias="listFolderId")]
    """The ID of the folder that the list should be created in.

    If left blank, then the list will be created in the root of the list folder
    structure.
    """

    list_permissions: Annotated[PublicListPermissionsParam, PropertyInfo(alias="listPermissions")]

    membership_settings: Annotated[PublicMembershipSettingsParam, PropertyInfo(alias="membershipSettings")]


FilterBranch: TypeAlias = Union[
    "PublicOrFilterBranchParam",
    "PublicAndFilterBranchParam",
    "PublicNotAllFilterBranchParam",
    "PublicNotAnyFilterBranchParam",
    "PublicRestrictedFilterBranchParam",
    "PublicUnifiedEventsFilterBranchParam",
    "PublicAssociationFilterBranchParam",
]

from .public_or_filter_branch_param import PublicOrFilterBranchParam
from .public_and_filter_branch_param import PublicAndFilterBranchParam
from .public_not_all_filter_branch_param import PublicNotAllFilterBranchParam
from .public_not_any_filter_branch_param import PublicNotAnyFilterBranchParam
from .public_restricted_filter_branch_param import PublicRestrictedFilterBranchParam
from .public_association_filter_branch_param import PublicAssociationFilterBranchParam
from .public_unified_events_filter_branch_param import PublicUnifiedEventsFilterBranchParam
