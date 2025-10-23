# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Optional
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["APIEventBasedEnrollmentCriteria", "ListMembershipFilterBranch", "RefinementCriteria"]

ListMembershipFilterBranch: TypeAlias = Union[
    "PublicOrFilterBranch",
    "PublicAndFilterBranch",
    "PublicNotAllFilterBranch",
    "PublicNotAnyFilterBranch",
    "PublicRestrictedFilterBranch",
    "PublicUnifiedEventsFilterBranch",
    "PublicPropertyAssociationFilterBranch",
    "PublicAssociationFilterBranch",
]

RefinementCriteria: TypeAlias = Union[
    "PublicOrFilterBranch",
    "PublicAndFilterBranch",
    "PublicNotAllFilterBranch",
    "PublicNotAnyFilterBranch",
    "PublicRestrictedFilterBranch",
    "PublicUnifiedEventsFilterBranch",
    "PublicPropertyAssociationFilterBranch",
    "PublicAssociationFilterBranch",
]


class APIEventBasedEnrollmentCriteria(BaseModel):
    event_filter_branches: List["PublicUnifiedEventsFilterBranch"] = FieldInfo(alias="eventFilterBranches")

    list_membership_filter_branches: List[ListMembershipFilterBranch] = FieldInfo(alias="listMembershipFilterBranches")
    """
    If you want to listen to list-membership events (an object was added to a list,
    an object was removed from a list) you need to use this
    `listMembershipFilterBranches` property instead of `eventFilterBranches`,
    because list membership events work differently.
    """

    should_re_enroll: bool = FieldInfo(alias="shouldReEnroll")
    """Whether or not the same object can enroll in this workflow twice."""

    type: Literal["EVENT_BASED"]
    """
    The type of enrollment criteria this is, this can be "LIST_BASED",
    "EVENT_BASED", or "MANUAL".
    """

    refinement_criteria: Optional[RefinementCriteria] = FieldInfo(alias="refinementCriteria", default=None)
    """List-based criteria to further refine which contacts will enroll in this flow."""


from ..shared.public_or_filter_branch import PublicOrFilterBranch
from ..shared.public_and_filter_branch import PublicAndFilterBranch
from ..shared.public_not_all_filter_branch import PublicNotAllFilterBranch
from ..shared.public_not_any_filter_branch import PublicNotAnyFilterBranch
from ..shared.public_restricted_filter_branch import PublicRestrictedFilterBranch
from ..shared.public_association_filter_branch import PublicAssociationFilterBranch
from ..shared.public_unified_events_filter_branch import PublicUnifiedEventsFilterBranch
from ..shared.public_property_association_filter_branch import PublicPropertyAssociationFilterBranch
