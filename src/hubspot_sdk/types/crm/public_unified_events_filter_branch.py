# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import TYPE_CHECKING, List, Union, Optional
from typing_extensions import Literal, TypeAlias, TypeAliasType

from pydantic import Field as FieldInfo

from ..._compat import PYDANTIC_V1
from ..._models import BaseModel
from .public_in_list_filter import PublicInListFilter
from .public_webinar_filter import PublicWebinarFilter
from .public_ads_time_filter import PublicAdsTimeFilter
from .public_constant_filter import PublicConstantFilter
from .public_property_filter import PublicPropertyFilter
from .public_ads_search_filter import PublicAdsSearchFilter
from .public_email_event_filter import PublicEmailEventFilter
from .public_cta_analytics_filter import PublicCtaAnalyticsFilter
from .public_survey_monkey_filter import PublicSurveyMonkeyFilter
from .public_time_point_operation import PublicTimePointOperation
from .public_all_history_refine_by import PublicAllHistoryRefineBy
from .public_ranged_time_operation import PublicRangedTimeOperation
from .public_unified_events_filter import PublicUnifiedEventsFilter
from .public_event_analytics_filter import PublicEventAnalyticsFilter
from .public_form_submission_filter import PublicFormSubmissionFilter
from .public_num_associations_filter import PublicNumAssociationsFilter
from .public_integration_event_filter import PublicIntegrationEventFilter
from .public_privacy_analytics_filter import PublicPrivacyAnalyticsFilter
from .public_email_subscription_filter import PublicEmailSubscriptionFilter
from .public_num_occurrences_refine_by import PublicNumOccurrencesRefineBy
from .public_set_occurrences_refine_by import PublicSetOccurrencesRefineBy
from .public_association_in_list_filter import PublicAssociationInListFilter
from .public_campaign_influenced_filter import PublicCampaignInfluencedFilter
from .public_page_view_analytics_filter import PublicPageViewAnalyticsFilter
from .public_survey_monkey_value_filter import PublicSurveyMonkeyValueFilter
from .public_form_submission_on_page_filter import PublicFormSubmissionOnPageFilter
from .public_communication_subscription_filter import PublicCommunicationSubscriptionFilter
from .public_absolute_ranged_timestamp_refine_by import PublicAbsoluteRangedTimestampRefineBy
from .public_property_association_in_list_filter import PublicPropertyAssociationInListFilter
from .public_relative_ranged_timestamp_refine_by import PublicRelativeRangedTimestampRefineBy
from .public_absolute_comparative_timestamp_refine_by import PublicAbsoluteComparativeTimestampRefineBy
from .public_relative_comparative_timestamp_refine_by import PublicRelativeComparativeTimestampRefineBy

__all__ = ["PublicUnifiedEventsFilterBranch", "FilterBranch", "Filter", "CoalescingRefineBy", "PruningRefineBy"]

if TYPE_CHECKING or not PYDANTIC_V1:
    FilterBranch = TypeAliasType(
        "FilterBranch",
        Union[
            "PublicOrFilterBranch",
            "PublicAndFilterBranch",
            "PublicNotAllFilterBranch",
            "PublicNotAnyFilterBranch",
            "PublicRestrictedFilterBranch",
            "PublicUnifiedEventsFilterBranch",
            "PublicPropertyAssociationFilterBranch",
            "PublicAssociationFilterBranch",
        ],
    )
else:
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

Filter: TypeAlias = Union[
    PublicPropertyFilter,
    PublicAssociationInListFilter,
    PublicPageViewAnalyticsFilter,
    PublicCtaAnalyticsFilter,
    PublicEventAnalyticsFilter,
    PublicFormSubmissionFilter,
    PublicFormSubmissionOnPageFilter,
    PublicIntegrationEventFilter,
    PublicEmailSubscriptionFilter,
    PublicCommunicationSubscriptionFilter,
    PublicCampaignInfluencedFilter,
    PublicSurveyMonkeyFilter,
    PublicSurveyMonkeyValueFilter,
    PublicWebinarFilter,
    PublicEmailEventFilter,
    PublicPrivacyAnalyticsFilter,
    PublicAdsSearchFilter,
    PublicAdsTimeFilter,
    PublicInListFilter,
    PublicNumAssociationsFilter,
    PublicUnifiedEventsFilter,
    PublicPropertyAssociationInListFilter,
    PublicConstantFilter,
]

CoalescingRefineBy: TypeAlias = Union[
    PublicNumOccurrencesRefineBy,
    PublicSetOccurrencesRefineBy,
    PublicRelativeComparativeTimestampRefineBy,
    PublicRelativeRangedTimestampRefineBy,
    PublicAbsoluteComparativeTimestampRefineBy,
    PublicAbsoluteRangedTimestampRefineBy,
    PublicAllHistoryRefineBy,
    PublicTimePointOperation,
    PublicRangedTimeOperation,
]

PruningRefineBy: TypeAlias = Union[
    PublicNumOccurrencesRefineBy,
    PublicSetOccurrencesRefineBy,
    PublicRelativeComparativeTimestampRefineBy,
    PublicRelativeRangedTimestampRefineBy,
    PublicAbsoluteComparativeTimestampRefineBy,
    PublicAbsoluteRangedTimestampRefineBy,
    PublicAllHistoryRefineBy,
    PublicTimePointOperation,
    PublicRangedTimeOperation,
]


class PublicUnifiedEventsFilterBranch(BaseModel):
    event_type_id: str = FieldInfo(alias="eventTypeId")
    """The identifier for the type of event associated with the filter branch."""

    filter_branches: List[FilterBranch] = FieldInfo(alias="filterBranches")

    filter_branch_operator: str = FieldInfo(alias="filterBranchOperator")
    """The logical operator used to combine filters within the branch (AND)."""

    filter_branch_type: Literal["UNIFIED_EVENTS"] = FieldInfo(alias="filterBranchType")
    """The type of the filter branch (UNIFIED_EVENTS)."""

    filters: List[Filter]

    operator: Literal["HAS_COMPLETED", "HAS_NOT_COMPLETED"]
    """
    Defines the operation to be applied within the filter branch (HAS_COMPLETED,
    HAS_NOT_COMPLETED).
    """

    coalescing_refine_by: Optional[CoalescingRefineBy] = FieldInfo(alias="coalescingRefineBy", default=None)
    """Specifies the criteria for refining the filter by coalescing."""

    pruning_refine_by: Optional[PruningRefineBy] = FieldInfo(alias="pruningRefineBy", default=None)


from .public_or_filter_branch import PublicOrFilterBranch
from .public_and_filter_branch import PublicAndFilterBranch
from .public_not_all_filter_branch import PublicNotAllFilterBranch
from .public_not_any_filter_branch import PublicNotAnyFilterBranch
from .public_restricted_filter_branch import PublicRestrictedFilterBranch
from .public_association_filter_branch import PublicAssociationFilterBranch
from .public_property_association_filter_branch import PublicPropertyAssociationFilterBranch
