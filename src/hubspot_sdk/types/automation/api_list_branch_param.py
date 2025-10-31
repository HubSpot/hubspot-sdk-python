# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Annotated, TypeAlias, TypedDict

from ..._utils import PropertyInfo
from .api_connection_param import APIConnectionParam

__all__ = ["APIListBranchParam", "FilterBranch"]

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


class APIListBranchParam(TypedDict, total=False):
    branch_name: Annotated[str, PropertyInfo(alias="branchName")]

    connection: APIConnectionParam

    filter_branch: Annotated[FilterBranch, PropertyInfo(alias="filterBranch")]


from ..shared_params.public_or_filter_branch import PublicOrFilterBranch
from ..shared_params.public_and_filter_branch import PublicAndFilterBranch
from ..shared_params.public_not_all_filter_branch import PublicNotAllFilterBranch
from ..shared_params.public_not_any_filter_branch import PublicNotAnyFilterBranch
from ..shared_params.public_restricted_filter_branch import PublicRestrictedFilterBranch
from ..shared_params.public_association_filter_branch import PublicAssociationFilterBranch
from ..shared_params.public_unified_events_filter_branch import PublicUnifiedEventsFilterBranch
from ..shared_params.public_property_association_filter_branch import PublicPropertyAssociationFilterBranch
