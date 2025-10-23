# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .api_time_window import APITimeWindow
from .api_blocked_date import APIBlockedDate
from .api_webhook_action import APIWebhookAction
from .api_custom_code_action import APICustomCodeAction
from .api_static_branch_action import APIStaticBranchAction
from .api_ab_test_branch_action import APIAbTestBranchAction
from .api_association_data_source import APIAssociationDataSource
from .api_single_connection_action import APISingleConnectionAction
from .api_daily_enrollment_schedule import APIDailyEnrollmentSchedule
from .api_manual_enrollment_criteria import APIManualEnrollmentCriteria
from .api_weekly_enrollment_schedule import APIWeeklyEnrollmentSchedule
from .api_yearly_enrollment_schedule import APIYearlyEnrollmentSchedule
from .api_association_timestamp_data_source import APIAssociationTimestampDataSource
from .api_property_based_enrollment_schedule import APIPropertyBasedEnrollmentSchedule
from .api_static_property_filter_data_source import APIStaticPropertyFilterDataSource
from .api_dataset_field_property_filter_data_source import APIDatasetFieldPropertyFilterDataSource
from .api_monthly_relative_days_enrollment_schedule import APIMonthlyRelativeDaysEnrollmentSchedule
from .api_monthly_specific_days_enrollment_schedule import APIMonthlySpecificDaysEnrollmentSchedule
from .api_enrolled_record_property_filter_data_source import APIEnrolledRecordPropertyFilterDataSource
from .api_enrolled_argument_property_filter_data_source import APIEnrolledArgumentPropertyFilterDataSource

__all__ = [
    "APIPlatformFlow",
    "Action",
    "DataSource",
    "EnrollmentCriteria",
    "EnrollmentSchedule",
    "SuppressionFilterBranch",
]

Action: TypeAlias = Union[
    APIStaticBranchAction,
    "APIListBranchAction",
    APIAbTestBranchAction,
    APICustomCodeAction,
    APIWebhookAction,
    APISingleConnectionAction,
]

DataSource: TypeAlias = Union[
    APIAssociationDataSource,
    APIAssociationTimestampDataSource,
    APIStaticPropertyFilterDataSource,
    APIEnrolledRecordPropertyFilterDataSource,
    APIDatasetFieldPropertyFilterDataSource,
    APIEnrolledArgumentPropertyFilterDataSource,
]

EnrollmentCriteria: TypeAlias = Union[
    "APIListBasedEnrollmentCriteria", "APIEventBasedEnrollmentCriteria", APIManualEnrollmentCriteria
]

EnrollmentSchedule: TypeAlias = Union[
    APIDailyEnrollmentSchedule,
    APIWeeklyEnrollmentSchedule,
    APIMonthlySpecificDaysEnrollmentSchedule,
    APIMonthlyRelativeDaysEnrollmentSchedule,
    APIYearlyEnrollmentSchedule,
    APIPropertyBasedEnrollmentSchedule,
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


class APIPlatformFlow(BaseModel):
    id: str

    actions: List[Action]

    blocked_dates: List[APIBlockedDate] = FieldInfo(alias="blockedDates")

    created_at: datetime = FieldInfo(alias="createdAt")

    crm_object_creation_status: Literal["PENDING", "COMPLETE"] = FieldInfo(alias="crmObjectCreationStatus")

    custom_properties: Dict[str, str] = FieldInfo(alias="customProperties")

    data_sources: List[DataSource] = FieldInfo(alias="dataSources")

    flow_type: Literal["WORKFLOW", "ACTION_SET", "UNKNOWN"] = FieldInfo(alias="flowType")

    is_enabled: bool = FieldInfo(alias="isEnabled")

    next_available_action_id: str = FieldInfo(alias="nextAvailableActionId")

    object_type_id: str = FieldInfo(alias="objectTypeId")

    revision_id: str = FieldInfo(alias="revisionId")

    time_windows: List[APITimeWindow] = FieldInfo(alias="timeWindows")

    type: Literal["CONTACT_FLOW", "PLATFORM_FLOW"]

    updated_at: datetime = FieldInfo(alias="updatedAt")

    description: Optional[str] = None

    enrollment_criteria: Optional[EnrollmentCriteria] = FieldInfo(alias="enrollmentCriteria", default=None)

    enrollment_schedule: Optional[EnrollmentSchedule] = FieldInfo(alias="enrollmentSchedule", default=None)

    name: Optional[str] = None

    start_action_id: Optional[str] = FieldInfo(alias="startActionId", default=None)

    suppression_filter_branch: Optional[SuppressionFilterBranch] = FieldInfo(
        alias="suppressionFilterBranch", default=None
    )

    uuid: Optional[str] = None


from .api_list_branch_action import APIListBranchAction
from ..shared.public_or_filter_branch import PublicOrFilterBranch
from ..shared.public_and_filter_branch import PublicAndFilterBranch
from .api_list_based_enrollment_criteria import APIListBasedEnrollmentCriteria
from .api_event_based_enrollment_criteria import APIEventBasedEnrollmentCriteria
from ..shared.public_not_all_filter_branch import PublicNotAllFilterBranch
from ..shared.public_not_any_filter_branch import PublicNotAnyFilterBranch
from ..shared.public_restricted_filter_branch import PublicRestrictedFilterBranch
from ..shared.public_association_filter_branch import PublicAssociationFilterBranch
from ..shared.public_unified_events_filter_branch import PublicUnifiedEventsFilterBranch
from ..shared.public_property_association_filter_branch import PublicPropertyAssociationFilterBranch
