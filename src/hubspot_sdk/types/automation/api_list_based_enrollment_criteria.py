# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["APIListBasedEnrollmentCriteria", "ListFilterBranch", "ReEnrollmentTriggersFilterBranch"]

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


class APIListBasedEnrollmentCriteria(BaseModel):
    list_filter_branch: ListFilterBranch = FieldInfo(alias="listFilterBranch")
    """The list filter branch that represents the enrollment trigger to this flow."""

    re_enrollment_triggers_filter_branches: List[ReEnrollmentTriggersFilterBranch] = FieldInfo(
        alias="reEnrollmentTriggersFilterBranches"
    )
    """
    A list of filter branches to listen for in order to re-enroll objects into this
    workflow.
    """

    should_re_enroll: bool = FieldInfo(alias="shouldReEnroll")
    """Whether or not the same object can enroll in this workflow twice."""

    type: Literal["LIST_BASED"]
    """
    The type of enrollment criteria this is, this can be "LIST_BASED",
    "EVENT_BASED", or "MANUAL".
    """

    un_enroll_objects_not_meeting_criteria: bool = FieldInfo(alias="unEnrollObjectsNotMeetingCriteria")
    """
    Whether or not to remove objects from this workflow if they stop meeting the
    enrollment criteria.
    """


from ..shared.public_or_filter_branch import PublicOrFilterBranch
from ..shared.public_and_filter_branch import PublicAndFilterBranch
from ..shared.public_not_all_filter_branch import PublicNotAllFilterBranch
from ..shared.public_not_any_filter_branch import PublicNotAnyFilterBranch
from ..shared.public_restricted_filter_branch import PublicRestrictedFilterBranch
from ..shared.public_association_filter_branch import PublicAssociationFilterBranch
from ..shared.public_unified_events_filter_branch import PublicUnifiedEventsFilterBranch
from ..shared.public_property_association_filter_branch import PublicPropertyAssociationFilterBranch
