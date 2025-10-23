# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from ..._utils import PropertyInfo

__all__ = ["APIListBasedEnrollmentCriteriaParam", "ListFilterBranch", "ReEnrollmentTriggersFilterBranch"]

ListFilterBranch: TypeAlias = Union[
    "PublicOrFilterBranch",
    "PublicAndFilterBranch",
    "PublicNotAllFilterBranch",
    "PublicNotAnyFilterBranch",
    "PublicRestrictedFilterBranch",
    "PublicUnifiedEventsFilterBranch",
    "PublicPropertyAssociationFilterBranch",
    "PublicAssociationFilterBranch",
]

ReEnrollmentTriggersFilterBranch: TypeAlias = Union[
    "PublicOrFilterBranch",
    "PublicAndFilterBranch",
    "PublicNotAllFilterBranch",
    "PublicNotAnyFilterBranch",
    "PublicRestrictedFilterBranch",
    "PublicUnifiedEventsFilterBranch",
    "PublicPropertyAssociationFilterBranch",
    "PublicAssociationFilterBranch",
]


class APIListBasedEnrollmentCriteriaParam(TypedDict, total=False):
    list_filter_branch: Required[Annotated[ListFilterBranch, PropertyInfo(alias="listFilterBranch")]]
    """The list filter branch that represents the enrollment trigger to this flow."""

    re_enrollment_triggers_filter_branches: Required[
        Annotated[Iterable[ReEnrollmentTriggersFilterBranch], PropertyInfo(alias="reEnrollmentTriggersFilterBranches")]
    ]
    """
    A list of filter branches to listen for in order to re-enroll objects into this
    workflow.
    """

    should_re_enroll: Required[Annotated[bool, PropertyInfo(alias="shouldReEnroll")]]
    """Whether or not the same object can enroll in this workflow twice."""

    type: Required[Literal["LIST_BASED"]]
    """
    The type of enrollment criteria this is, this can be "LIST_BASED",
    "EVENT_BASED", or "MANUAL".
    """

    un_enroll_objects_not_meeting_criteria: Required[
        Annotated[bool, PropertyInfo(alias="unEnrollObjectsNotMeetingCriteria")]
    ]
    """
    Whether or not to remove objects from this workflow if they stop meeting the
    enrollment criteria.
    """


from ..shared_params.public_or_filter_branch import PublicOrFilterBranch
from ..shared_params.public_and_filter_branch import PublicAndFilterBranch
from ..shared_params.public_not_all_filter_branch import PublicNotAllFilterBranch
from ..shared_params.public_not_any_filter_branch import PublicNotAnyFilterBranch
from ..shared_params.public_restricted_filter_branch import PublicRestrictedFilterBranch
from ..shared_params.public_association_filter_branch import PublicAssociationFilterBranch
from ..shared_params.public_unified_events_filter_branch import PublicUnifiedEventsFilterBranch
from ..shared_params.public_property_association_filter_branch import PublicPropertyAssociationFilterBranch
