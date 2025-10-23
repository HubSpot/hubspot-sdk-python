# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from ..._utils import PropertyInfo
from .api_time_window_param import APITimeWindowParam
from .api_blocked_date_param import APIBlockedDateParam
from .api_webhook_action_param import APIWebhookActionParam
from .api_custom_code_action_param import APICustomCodeActionParam
from .api_static_branch_action_param import APIStaticBranchActionParam
from .api_ab_test_branch_action_param import APIAbTestBranchActionParam
from .api_association_data_source_param import APIAssociationDataSourceParam
from .api_single_connection_action_param import APISingleConnectionActionParam
from .api_daily_enrollment_schedule_param import APIDailyEnrollmentScheduleParam
from .api_manual_enrollment_criteria_param import APIManualEnrollmentCriteriaParam
from .api_weekly_enrollment_schedule_param import APIWeeklyEnrollmentScheduleParam
from .api_yearly_enrollment_schedule_param import APIYearlyEnrollmentScheduleParam
from .api_association_timestamp_data_source_param import APIAssociationTimestampDataSourceParam
from .api_property_based_enrollment_schedule_param import APIPropertyBasedEnrollmentScheduleParam
from .api_static_property_filter_data_source_param import APIStaticPropertyFilterDataSourceParam
from .api_dataset_field_property_filter_data_source_param import APIDatasetFieldPropertyFilterDataSourceParam
from .api_monthly_relative_days_enrollment_schedule_param import APIMonthlyRelativeDaysEnrollmentScheduleParam
from .api_monthly_specific_days_enrollment_schedule_param import APIMonthlySpecificDaysEnrollmentScheduleParam
from .api_enrolled_record_property_filter_data_source_param import APIEnrolledRecordPropertyFilterDataSourceParam
from .api_enrolled_argument_property_filter_data_source_param import APIEnrolledArgumentPropertyFilterDataSourceParam

__all__ = [
    "APIPlatformFlowCreateRequestParam",
    "Action",
    "DataSource",
    "EnrollmentCriteria",
    "EnrollmentSchedule",
    "SuppressionFilterBranch",
]

Action: TypeAlias = Union[
    APIStaticBranchActionParam,
    "APIListBranchActionParam",
    APIAbTestBranchActionParam,
    APICustomCodeActionParam,
    APIWebhookActionParam,
    APISingleConnectionActionParam,
]

DataSource: TypeAlias = Union[
    APIAssociationDataSourceParam,
    APIAssociationTimestampDataSourceParam,
    APIStaticPropertyFilterDataSourceParam,
    APIEnrolledRecordPropertyFilterDataSourceParam,
    APIDatasetFieldPropertyFilterDataSourceParam,
    APIEnrolledArgumentPropertyFilterDataSourceParam,
]

EnrollmentCriteria: TypeAlias = Union[
    "APIListBasedEnrollmentCriteriaParam", "APIEventBasedEnrollmentCriteriaParam", APIManualEnrollmentCriteriaParam
]

EnrollmentSchedule: TypeAlias = Union[
    APIDailyEnrollmentScheduleParam,
    APIWeeklyEnrollmentScheduleParam,
    APIMonthlySpecificDaysEnrollmentScheduleParam,
    APIMonthlyRelativeDaysEnrollmentScheduleParam,
    APIYearlyEnrollmentScheduleParam,
    APIPropertyBasedEnrollmentScheduleParam,
]

SuppressionFilterBranch: TypeAlias = Union[
    "PublicOrFilterBranch",
    "PublicAndFilterBranch",
    "PublicNotAllFilterBranch",
    "PublicNotAnyFilterBranch",
    "PublicRestrictedFilterBranch",
    "PublicUnifiedEventsFilterBranch",
    "PublicPropertyAssociationFilterBranch",
    "PublicAssociationFilterBranch",
]


class APIPlatformFlowCreateRequestParam(TypedDict, total=False):
    actions: Required[Iterable[Action]]

    blocked_dates: Required[Annotated[Iterable[APIBlockedDateParam], PropertyInfo(alias="blockedDates")]]

    custom_properties: Required[Annotated[Dict[str, str], PropertyInfo(alias="customProperties")]]

    data_sources: Required[Annotated[Iterable[DataSource], PropertyInfo(alias="dataSources")]]

    flow_type: Required[Annotated[Literal["WORKFLOW", "ACTION_SET", "UNKNOWN"], PropertyInfo(alias="flowType")]]

    is_enabled: Required[Annotated[bool, PropertyInfo(alias="isEnabled")]]

    object_type_id: Required[Annotated[str, PropertyInfo(alias="objectTypeId")]]

    time_windows: Required[Annotated[Iterable[APITimeWindowParam], PropertyInfo(alias="timeWindows")]]

    type: Required[Literal["CONTACT_FLOW", "PLATFORM_FLOW"]]

    description: str

    enrollment_criteria: Annotated[EnrollmentCriteria, PropertyInfo(alias="enrollmentCriteria")]

    enrollment_schedule: Annotated[EnrollmentSchedule, PropertyInfo(alias="enrollmentSchedule")]

    name: str

    start_action_id: Annotated[str, PropertyInfo(alias="startActionId")]

    suppression_filter_branch: Annotated[SuppressionFilterBranch, PropertyInfo(alias="suppressionFilterBranch")]

    uuid: str


from .api_list_branch_action_param import APIListBranchActionParam
from ..shared_params.public_or_filter_branch import PublicOrFilterBranch
from ..shared_params.public_and_filter_branch import PublicAndFilterBranch
from .api_list_based_enrollment_criteria_param import APIListBasedEnrollmentCriteriaParam
from .api_event_based_enrollment_criteria_param import APIEventBasedEnrollmentCriteriaParam
from ..shared_params.public_not_all_filter_branch import PublicNotAllFilterBranch
from ..shared_params.public_not_any_filter_branch import PublicNotAnyFilterBranch
from ..shared_params.public_restricted_filter_branch import PublicRestrictedFilterBranch
from ..shared_params.public_association_filter_branch import PublicAssociationFilterBranch
from ..shared_params.public_unified_events_filter_branch import PublicUnifiedEventsFilterBranch
from ..shared_params.public_property_association_filter_branch import PublicPropertyAssociationFilterBranch
