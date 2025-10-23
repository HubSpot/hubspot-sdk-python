# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import TYPE_CHECKING, Union, Iterable
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict, TypeAliasType

from ..._utils import PropertyInfo
from ..._compat import PYDANTIC_V1
from .public_in_list_filter import PublicInListFilter
from .public_webinar_filter import PublicWebinarFilter
from .public_ads_time_filter import PublicAdsTimeFilter
from .public_constant_filter import PublicConstantFilter
from .public_property_filter import PublicPropertyFilter
from .public_ads_search_filter import PublicAdsSearchFilter
from .public_email_event_filter import PublicEmailEventFilter
from .public_cta_analytics_filter import PublicCtaAnalyticsFilter
from .public_survey_monkey_filter import PublicSurveyMonkeyFilter
from .public_unified_events_filter import PublicUnifiedEventsFilter
from .public_event_analytics_filter import PublicEventAnalyticsFilter
from .public_form_submission_filter import PublicFormSubmissionFilter
from .public_num_associations_filter import PublicNumAssociationsFilter
from .public_integration_event_filter import PublicIntegrationEventFilter
from .public_privacy_analytics_filter import PublicPrivacyAnalyticsFilter
from .public_email_subscription_filter import PublicEmailSubscriptionFilter
from .public_association_in_list_filter import PublicAssociationInListFilter
from .public_campaign_influenced_filter import PublicCampaignInfluencedFilter
from .public_page_view_analytics_filter import PublicPageViewAnalyticsFilter
from .public_survey_monkey_value_filter import PublicSurveyMonkeyValueFilter
from .public_form_submission_on_page_filter import PublicFormSubmissionOnPageFilter
from .public_communication_subscription_filter import PublicCommunicationSubscriptionFilter
from .public_property_association_in_list_filter import PublicPropertyAssociationInListFilter

__all__ = ["PublicAndFilterBranch", "FilterBranch", "Filter"]

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


class PublicAndFilterBranch(TypedDict, total=False):
    filter_branches: Required[Annotated[Iterable[FilterBranch], PropertyInfo(alias="filterBranches")]]

    filter_branch_operator: Required[Annotated[str, PropertyInfo(alias="filterBranchOperator")]]

    filter_branch_type: Required[Annotated[Literal["AND"], PropertyInfo(alias="filterBranchType")]]

    filters: Required[Iterable[Filter]]


from .public_or_filter_branch import PublicOrFilterBranch
from .public_not_all_filter_branch import PublicNotAllFilterBranch
from .public_not_any_filter_branch import PublicNotAnyFilterBranch
from .public_restricted_filter_branch import PublicRestrictedFilterBranch
from .public_association_filter_branch import PublicAssociationFilterBranch
from .public_unified_events_filter_branch import PublicUnifiedEventsFilterBranch
from .public_property_association_filter_branch import PublicPropertyAssociationFilterBranch
