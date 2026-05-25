# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import TYPE_CHECKING, List, Union
from typing_extensions import Literal, Annotated, TypeAlias, TypeAliasType

from pydantic import Field as FieldInfo

from ..._utils import PropertyInfo
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
from .public_unified_events_filter import PublicUnifiedEventsFilter
from .public_event_analytics_filter import PublicEventAnalyticsFilter
from .public_form_submission_filter import PublicFormSubmissionFilter
from .public_integration_event_filter import PublicIntegrationEventFilter
from .public_privacy_analytics_filter import PublicPrivacyAnalyticsFilter
from .public_email_subscription_filter import PublicEmailSubscriptionFilter
from .public_association_in_list_filter import PublicAssociationInListFilter
from .public_page_view_analytics_filter import PublicPageViewAnalyticsFilter
from .public_survey_monkey_value_filter import PublicSurveyMonkeyValueFilter
from .public_form_submission_on_page_filter import PublicFormSubmissionOnPageFilter
from .public_communication_subscription_filter import PublicCommunicationSubscriptionFilter

__all__ = ["PublicNotAnyFilterBranch", "FilterBranch", "Filter"]

if TYPE_CHECKING or not PYDANTIC_V1:
    FilterBranch = TypeAliasType(
        "FilterBranch",
        Annotated[
            Union[
                "PublicOrFilterBranch",
                "PublicAndFilterBranch",
                "PublicNotAllFilterBranch",
                "PublicNotAnyFilterBranch",
                "PublicRestrictedFilterBranch",
                "PublicUnifiedEventsFilterBranch",
                "PublicAssociationFilterBranch",
            ],
            PropertyInfo(discriminator="filter_branch_type"),
        ],
    )
else:
    FilterBranch: TypeAlias = Annotated[
        Union[
            "PublicOrFilterBranch",
            "PublicAndFilterBranch",
            "PublicNotAllFilterBranch",
            "PublicNotAnyFilterBranch",
            "PublicRestrictedFilterBranch",
            "PublicUnifiedEventsFilterBranch",
            "PublicAssociationFilterBranch",
        ],
        PropertyInfo(discriminator="filter_branch_type"),
    ]

Filter: TypeAlias = Annotated[
    Union[
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
        PublicSurveyMonkeyFilter,
        PublicSurveyMonkeyValueFilter,
        PublicWebinarFilter,
        PublicEmailEventFilter,
        PublicPrivacyAnalyticsFilter,
        PublicAdsSearchFilter,
        PublicAdsTimeFilter,
        PublicInListFilter,
        PublicUnifiedEventsFilter,
        PublicConstantFilter,
    ],
    PropertyInfo(discriminator="filter_type"),
]


class PublicNotAnyFilterBranch(BaseModel):
    filter_branches: List[FilterBranch] = FieldInfo(alias="filterBranches")

    filter_branch_operator: str = FieldInfo(alias="filterBranchOperator")
    """
    Specifies the logical operator used to combine filters within the branch
    (NOT_ANY).
    """

    filter_branch_type: Literal["NOT_ANY"] = FieldInfo(alias="filterBranchType")
    """Indicates the type of filter branch (NOT_ANY)."""

    filters: List[Filter]


from .public_or_filter_branch import PublicOrFilterBranch
from .public_and_filter_branch import PublicAndFilterBranch
from .public_not_all_filter_branch import PublicNotAllFilterBranch
from .public_restricted_filter_branch import PublicRestrictedFilterBranch
from .public_association_filter_branch import PublicAssociationFilterBranch
from .public_unified_events_filter_branch import PublicUnifiedEventsFilterBranch
