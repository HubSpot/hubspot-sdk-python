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

    re_enrollment_triggers_filter_branches: Required[
        Annotated[Iterable[ReEnrollmentTriggersFilterBranch], PropertyInfo(alias="reEnrollmentTriggersFilterBranches")]
    ]

    should_re_enroll: Required[Annotated[bool, PropertyInfo(alias="shouldReEnroll")]]

    type: Required[Literal["LIST_BASED"]]

    un_enroll_objects_not_meeting_criteria: Required[
        Annotated[bool, PropertyInfo(alias="unEnrollObjectsNotMeetingCriteria")]
    ]


from ..shared_params.public_or_filter_branch import PublicOrFilterBranch
from ..shared_params.public_and_filter_branch import PublicAndFilterBranch
from ..shared_params.public_not_all_filter_branch import PublicNotAllFilterBranch
from ..shared_params.public_not_any_filter_branch import PublicNotAnyFilterBranch
from ..shared_params.public_restricted_filter_branch import PublicRestrictedFilterBranch
from ..shared_params.public_association_filter_branch import PublicAssociationFilterBranch
from ..shared_params.public_unified_events_filter_branch import PublicUnifiedEventsFilterBranch
from ..shared_params.public_property_association_filter_branch import PublicPropertyAssociationFilterBranch
