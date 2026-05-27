# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import TYPE_CHECKING, Union, Iterable
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict, TypeAliasType

from ..._utils import PropertyInfo
from ..._compat import PYDANTIC_V1
from .public_in_list_filter_param import PublicInListFilterParam
from .public_webinar_filter_param import PublicWebinarFilterParam
from .public_ads_time_filter_param import PublicAdsTimeFilterParam
from .public_constant_filter_param import PublicConstantFilterParam
from .public_property_filter_param import PublicPropertyFilterParam
from .public_ads_search_filter_param import PublicAdsSearchFilterParam
from .public_email_event_filter_param import PublicEmailEventFilterParam
from .public_cta_analytics_filter_param import PublicCtaAnalyticsFilterParam
from .public_survey_monkey_filter_param import PublicSurveyMonkeyFilterParam
from .public_time_point_operation_param import PublicTimePointOperationParam
from .public_all_history_refine_by_param import PublicAllHistoryRefineByParam
from .public_ranged_time_operation_param import PublicRangedTimeOperationParam
from .public_unified_events_filter_param import PublicUnifiedEventsFilterParam
from .public_event_analytics_filter_param import PublicEventAnalyticsFilterParam
from .public_form_submission_filter_param import PublicFormSubmissionFilterParam
from .public_integration_event_filter_param import PublicIntegrationEventFilterParam
from .public_privacy_analytics_filter_param import PublicPrivacyAnalyticsFilterParam
from .public_email_subscription_filter_param import PublicEmailSubscriptionFilterParam
from .public_num_occurrences_refine_by_param import PublicNumOccurrencesRefineByParam
from .public_set_occurrences_refine_by_param import PublicSetOccurrencesRefineByParam
from .public_association_in_list_filter_param import PublicAssociationInListFilterParam
from .public_page_view_analytics_filter_param import PublicPageViewAnalyticsFilterParam
from .public_survey_monkey_value_filter_param import PublicSurveyMonkeyValueFilterParam
from .public_form_submission_on_page_filter_param import PublicFormSubmissionOnPageFilterParam
from .public_communication_subscription_filter_param import PublicCommunicationSubscriptionFilterParam
from .public_absolute_ranged_timestamp_refine_by_param import PublicAbsoluteRangedTimestampRefineByParam
from .public_relative_ranged_timestamp_refine_by_param import PublicRelativeRangedTimestampRefineByParam
from .public_absolute_comparative_timestamp_refine_by_param import PublicAbsoluteComparativeTimestampRefineByParam
from .public_relative_comparative_timestamp_refine_by_param import PublicRelativeComparativeTimestampRefineByParam

__all__ = ["PublicUnifiedEventsFilterBranchParam", "FilterBranch", "Filter", "CoalescingRefineBy", "PruningRefineBy"]

if TYPE_CHECKING or not PYDANTIC_V1:
    FilterBranch = TypeAliasType(
        "FilterBranch",
        Union[
            "PublicOrFilterBranchParam",
            "PublicAndFilterBranchParam",
            "PublicNotAllFilterBranchParam",
            "PublicNotAnyFilterBranchParam",
            "PublicRestrictedFilterBranchParam",
            "PublicUnifiedEventsFilterBranchParam",
            "PublicAssociationFilterBranchParam",
        ],
    )
else:
    FilterBranch: TypeAlias = Union[
        "PublicOrFilterBranchParam",
        "PublicAndFilterBranchParam",
        "PublicNotAllFilterBranchParam",
        "PublicNotAnyFilterBranchParam",
        "PublicRestrictedFilterBranchParam",
        "PublicUnifiedEventsFilterBranchParam",
        "PublicAssociationFilterBranchParam",
    ]

Filter: TypeAlias = Union[
    PublicPropertyFilterParam,
    PublicAssociationInListFilterParam,
    PublicPageViewAnalyticsFilterParam,
    PublicCtaAnalyticsFilterParam,
    PublicEventAnalyticsFilterParam,
    PublicFormSubmissionFilterParam,
    PublicFormSubmissionOnPageFilterParam,
    PublicIntegrationEventFilterParam,
    PublicEmailSubscriptionFilterParam,
    PublicCommunicationSubscriptionFilterParam,
    PublicSurveyMonkeyFilterParam,
    PublicSurveyMonkeyValueFilterParam,
    PublicWebinarFilterParam,
    PublicEmailEventFilterParam,
    PublicPrivacyAnalyticsFilterParam,
    PublicAdsSearchFilterParam,
    PublicAdsTimeFilterParam,
    PublicInListFilterParam,
    PublicUnifiedEventsFilterParam,
    PublicConstantFilterParam,
]

CoalescingRefineBy: TypeAlias = Union[
    PublicNumOccurrencesRefineByParam,
    PublicSetOccurrencesRefineByParam,
    PublicRelativeComparativeTimestampRefineByParam,
    PublicRelativeRangedTimestampRefineByParam,
    PublicAbsoluteComparativeTimestampRefineByParam,
    PublicAbsoluteRangedTimestampRefineByParam,
    PublicAllHistoryRefineByParam,
    PublicTimePointOperationParam,
    PublicRangedTimeOperationParam,
]

PruningRefineBy: TypeAlias = Union[
    PublicNumOccurrencesRefineByParam,
    PublicSetOccurrencesRefineByParam,
    PublicRelativeComparativeTimestampRefineByParam,
    PublicRelativeRangedTimestampRefineByParam,
    PublicAbsoluteComparativeTimestampRefineByParam,
    PublicAbsoluteRangedTimestampRefineByParam,
    PublicAllHistoryRefineByParam,
    PublicTimePointOperationParam,
    PublicRangedTimeOperationParam,
]


class PublicUnifiedEventsFilterBranchParam(TypedDict, total=False):
    event_type_id: Required[Annotated[str, PropertyInfo(alias="eventTypeId")]]
    """The identifier for the type of event associated with the filter branch."""

    filter_branches: Required[Annotated[Iterable[FilterBranch], PropertyInfo(alias="filterBranches")]]

    filter_branch_operator: Required[Annotated[str, PropertyInfo(alias="filterBranchOperator")]]
    """The logical operator used to combine filters within the branch (AND)."""

    filter_branch_type: Required[Annotated[Literal["UNIFIED_EVENTS"], PropertyInfo(alias="filterBranchType")]]
    """The type of the filter branch (UNIFIED_EVENTS)."""

    filters: Required[Iterable[Filter]]

    operator: Required[Literal["HAS_COMPLETED", "HAS_NOT_COMPLETED"]]
    """
    Defines the operation to be applied within the filter branch (HAS_COMPLETED,
    HAS_NOT_COMPLETED).
    """

    coalescing_refine_by: Annotated[CoalescingRefineBy, PropertyInfo(alias="coalescingRefineBy")]
    """Specifies the criteria for refining the filter by coalescing."""

    pruning_refine_by: Annotated[PruningRefineBy, PropertyInfo(alias="pruningRefineBy")]


from .public_or_filter_branch_param import PublicOrFilterBranchParam
from .public_and_filter_branch_param import PublicAndFilterBranchParam
from .public_not_all_filter_branch_param import PublicNotAllFilterBranchParam
from .public_not_any_filter_branch_param import PublicNotAnyFilterBranchParam
from .public_restricted_filter_branch_param import PublicRestrictedFilterBranchParam
from .public_association_filter_branch_param import PublicAssociationFilterBranchParam
