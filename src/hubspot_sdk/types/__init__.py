# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from . import shared
from .. import _compat
from .shared import (
    Error as Error,
    Paging as Paging,
    NextPage as NextPage,
    ErrorDetail as ErrorDetail,
    TaskLocator as TaskLocator,
    VersionUser as VersionUser,
    PreviousPage as PreviousPage,
    ForwardPaging as ForwardPaging,
    StandardError as StandardError,
    ActionResponse as ActionResponse,
    PublicObjectID as PublicObjectID,
    AssociationSpec as AssociationSpec,
    PublicDatePoint as PublicDatePoint,
    BatchInputString as BatchInputString,
    PublicTimeOffset as PublicTimeOffset,
    PublicIndexOffset as PublicIndexOffset,
    PublicInListFilter as PublicInListFilter,
    PublicNowReference as PublicNowReference,
    PublicAdsTimeFilter as PublicAdsTimeFilter,
    PublicWebinarFilter as PublicWebinarFilter,
    PublicWeekReference as PublicWeekReference,
    PublicYearReference as PublicYearReference,
    PublicConstantFilter as PublicConstantFilter,
    PublicMonthReference as PublicMonthReference,
    PublicOrFilterBranch as PublicOrFilterBranch,
    PublicPropertyFilter as PublicPropertyFilter,
    PublicTodayReference as PublicTodayReference,
    PublicAdsSearchFilter as PublicAdsSearchFilter,
    PublicAndFilterBranch as PublicAndFilterBranch,
    HubDBTableRowV3Wrapper as HubDBTableRowV3Wrapper,
    PublicEmailEventFilter as PublicEmailEventFilter,
    PublicIndexedTimePoint as PublicIndexedTimePoint,
    PublicQuarterReference as PublicQuarterReference,
    AbTestCreateRequestVNext as AbTestCreateRequestVNext,
    PublicAllHistoryRefineBy as PublicAllHistoryRefineBy,
    PublicCtaAnalyticsFilter as PublicCtaAnalyticsFilter,
    PublicNotAllFilterBranch as PublicNotAllFilterBranch,
    PublicNotAnyFilterBranch as PublicNotAnyFilterBranch,
    PublicSurveyMonkeyFilter as PublicSurveyMonkeyFilter,
    PublicTimePointOperation as PublicTimePointOperation,
    PublicEventFilterMetadata as PublicEventFilterMetadata,
    PublicFiscalYearReference as PublicFiscalYearReference,
    PublicRangedTimeOperation as PublicRangedTimeOperation,
    PublicUnifiedEventsFilter as PublicUnifiedEventsFilter,
    PublicEventAnalyticsFilter as PublicEventAnalyticsFilter,
    PublicFormSubmissionFilter as PublicFormSubmissionFilter,
    PublicInListFilterMetadata as PublicInListFilterMetadata,
    PublicBoolPropertyOperation as PublicBoolPropertyOperation,
    PublicDatePropertyOperation as PublicDatePropertyOperation,
    PublicNumAssociationsFilter as PublicNumAssociationsFilter,
    PublicFiscalQuarterReference as PublicFiscalQuarterReference,
    PublicIntegrationEventFilter as PublicIntegrationEventFilter,
    PublicNumOccurrencesRefineBy as PublicNumOccurrencesRefineBy,
    PublicPrivacyAnalyticsFilter as PublicPrivacyAnalyticsFilter,
    PublicPropertyReferencedTime as PublicPropertyReferencedTime,
    PublicRestrictedFilterBranch as PublicRestrictedFilterBranch,
    PublicSetOccurrencesRefineBy as PublicSetOccurrencesRefineBy,
    PublicAssociationFilterBranch as PublicAssociationFilterBranch,
    PublicAssociationInListFilter as PublicAssociationInListFilter,
    PublicEmailSubscriptionFilter as PublicEmailSubscriptionFilter,
    PublicNumberPropertyOperation as PublicNumberPropertyOperation,
    PublicPageViewAnalyticsFilter as PublicPageViewAnalyticsFilter,
    PublicStringPropertyOperation as PublicStringPropertyOperation,
    PublicSurveyMonkeyValueFilter as PublicSurveyMonkeyValueFilter,
    PublicCampaignInfluencedFilter as PublicCampaignInfluencedFilter,
    PublicAllPropertyTypesOperation as PublicAllPropertyTypesOperation,
    PublicDateTimePropertyOperation as PublicDateTimePropertyOperation,
    PublicUnifiedEventsFilterBranch as PublicUnifiedEventsFilterBranch,
    PublicFormSubmissionOnPageFilter as PublicFormSubmissionOnPageFilter,
    PublicRangedDatePropertyOperation as PublicRangedDatePropertyOperation,
    PublicEnumerationPropertyOperation as PublicEnumerationPropertyOperation,
    PublicMultiStringPropertyOperation as PublicMultiStringPropertyOperation,
    PublicCalendarDatePropertyOperation as PublicCalendarDatePropertyOperation,
    PublicRangedNumberPropertyOperation as PublicRangedNumberPropertyOperation,
    PublicAbsoluteRangedTimestampRefineBy as PublicAbsoluteRangedTimestampRefineBy,
    PublicCommunicationSubscriptionFilter as PublicCommunicationSubscriptionFilter,
    PublicPropertyAssociationFilterBranch as PublicPropertyAssociationFilterBranch,
    PublicPropertyAssociationInListFilter as PublicPropertyAssociationInListFilter,
    PublicRelativeRangedTimestampRefineBy as PublicRelativeRangedTimestampRefineBy,
    PublicRollingPropertyUpdatedOperation as PublicRollingPropertyUpdatedOperation,
    PublicComparativeDatePropertyOperation as PublicComparativeDatePropertyOperation,
    PublicRollingDateRangePropertyOperation as PublicRollingDateRangePropertyOperation,
    PublicComparativePropertyUpdatedOperation as PublicComparativePropertyUpdatedOperation,
    PublicAbsoluteComparativeTimestampRefineBy as PublicAbsoluteComparativeTimestampRefineBy,
    PublicRelativeComparativeTimestampRefineBy as PublicRelativeComparativeTimestampRefineBy,
)

# Rebuild cyclical models only after all modules are imported.
# This ensures that, when building the deferred (due to cyclical references) model schema,
# Pydantic can resolve the necessary references.
# See: https://github.com/pydantic/pydantic/issues/11250 for more context.
if _compat.PYDANTIC_V1:
    shared.public_and_filter_branch.PublicAndFilterBranch.update_forward_refs()  # type: ignore
    shared.public_association_filter_branch.PublicAssociationFilterBranch.update_forward_refs()  # type: ignore
    shared.public_not_all_filter_branch.PublicNotAllFilterBranch.update_forward_refs()  # type: ignore
    shared.public_not_any_filter_branch.PublicNotAnyFilterBranch.update_forward_refs()  # type: ignore
    shared.public_or_filter_branch.PublicOrFilterBranch.update_forward_refs()  # type: ignore
    shared.public_property_association_filter_branch.PublicPropertyAssociationFilterBranch.update_forward_refs()  # type: ignore
    shared.public_restricted_filter_branch.PublicRestrictedFilterBranch.update_forward_refs()  # type: ignore
    shared.public_unified_events_filter_branch.PublicUnifiedEventsFilterBranch.update_forward_refs()  # type: ignore
else:
    shared.public_and_filter_branch.PublicAndFilterBranch.model_rebuild(_parent_namespace_depth=0)
    shared.public_association_filter_branch.PublicAssociationFilterBranch.model_rebuild(_parent_namespace_depth=0)
    shared.public_not_all_filter_branch.PublicNotAllFilterBranch.model_rebuild(_parent_namespace_depth=0)
    shared.public_not_any_filter_branch.PublicNotAnyFilterBranch.model_rebuild(_parent_namespace_depth=0)
    shared.public_or_filter_branch.PublicOrFilterBranch.model_rebuild(_parent_namespace_depth=0)
    shared.public_property_association_filter_branch.PublicPropertyAssociationFilterBranch.model_rebuild(
        _parent_namespace_depth=0
    )
    shared.public_restricted_filter_branch.PublicRestrictedFilterBranch.model_rebuild(_parent_namespace_depth=0)
    shared.public_unified_events_filter_branch.PublicUnifiedEventsFilterBranch.model_rebuild(_parent_namespace_depth=0)
