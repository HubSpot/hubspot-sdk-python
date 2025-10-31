# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from typing_extensions import TypeAlias

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .api_connection import APIConnection

__all__ = ["APIListBranch", "FilterBranch"]

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


class APIListBranch(BaseModel):
    branch_name: Optional[str] = FieldInfo(alias="branchName", default=None)

    connection: Optional[APIConnection] = None

    filter_branch: Optional[FilterBranch] = FieldInfo(alias="filterBranch", default=None)


from ..shared.public_or_filter_branch import PublicOrFilterBranch
from ..shared.public_and_filter_branch import PublicAndFilterBranch
from ..shared.public_not_all_filter_branch import PublicNotAllFilterBranch
from ..shared.public_not_any_filter_branch import PublicNotAnyFilterBranch
from ..shared.public_restricted_filter_branch import PublicRestrictedFilterBranch
from ..shared.public_association_filter_branch import PublicAssociationFilterBranch
from ..shared.public_unified_events_filter_branch import PublicUnifiedEventsFilterBranch
from ..shared.public_property_association_filter_branch import PublicPropertyAssociationFilterBranch
