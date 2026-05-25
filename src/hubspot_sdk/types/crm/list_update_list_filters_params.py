# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Required, Annotated, TypeAlias, TypedDict

from ..._utils import PropertyInfo

__all__ = ["ListUpdateListFiltersParams", "FilterBranch"]


class ListUpdateListFiltersParams(TypedDict, total=False):
    filter_branch: Required[Annotated[FilterBranch, PropertyInfo(alias="filterBranch")]]
    """Updated filtering criteria for the list"""

    enroll_objects_in_workflows: Annotated[bool, PropertyInfo(alias="enrollObjectsInWorkflows")]


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
