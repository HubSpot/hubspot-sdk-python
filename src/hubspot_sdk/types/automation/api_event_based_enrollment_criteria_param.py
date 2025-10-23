# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from ..._utils import PropertyInfo

__all__ = ["APIEventBasedEnrollmentCriteriaParam", "ListMembershipFilterBranch", "RefinementCriteria"]

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


class APIEventBasedEnrollmentCriteriaParam(TypedDict, total=False):
    event_filter_branches: Required[
        Annotated[Iterable["PublicUnifiedEventsFilterBranch"], PropertyInfo(alias="eventFilterBranches")]
    ]

    list_membership_filter_branches: Required[
        Annotated[Iterable[ListMembershipFilterBranch], PropertyInfo(alias="listMembershipFilterBranches")]
    ]
    """
    If you want to listen to list-membership events (an object was added to a list,
    an object was removed from a list) you need to use this
    `listMembershipFilterBranches` property instead of `eventFilterBranches`,
    because list membership events work differently.
    """

    should_re_enroll: Required[Annotated[bool, PropertyInfo(alias="shouldReEnroll")]]
    """Whether or not the same object can enroll in this workflow twice."""

    type: Required[Literal["EVENT_BASED"]]
    """
    The type of enrollment criteria this is, this can be "LIST_BASED",
    "EVENT_BASED", or "MANUAL".
    """

    refinement_criteria: Annotated[RefinementCriteria, PropertyInfo(alias="refinementCriteria")]
    """List-based criteria to further refine which contacts will enroll in this flow."""


from ..shared_params.public_or_filter_branch import PublicOrFilterBranch
from ..shared_params.public_and_filter_branch import PublicAndFilterBranch
from ..shared_params.public_not_all_filter_branch import PublicNotAllFilterBranch
from ..shared_params.public_not_any_filter_branch import PublicNotAnyFilterBranch
from ..shared_params.public_restricted_filter_branch import PublicRestrictedFilterBranch
from ..shared_params.public_association_filter_branch import PublicAssociationFilterBranch
from ..shared_params.public_unified_events_filter_branch import PublicUnifiedEventsFilterBranch
from ..shared_params.public_property_association_filter_branch import PublicPropertyAssociationFilterBranch
