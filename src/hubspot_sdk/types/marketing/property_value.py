# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["PropertyValue"]


class PropertyValue(BaseModel):
    name: str
    """Name of custom property"""

    source_upstream_deployable: str = FieldInfo(alias="sourceUpstreamDeployable")

    value: str
    """Custom property value"""

    data_sensitivity: Optional[Literal["none", "standard", "high"]] = FieldInfo(alias="dataSensitivity", default=None)
    """
    The sensitivity level of the property, such as "non_sensitive", "sensitive", and
    "highly_sensitive".
    """

    is_encrypted: Optional[bool] = FieldInfo(alias="isEncrypted", default=None)
    """Whether the property value is encrypted."""

    is_large_value: Optional[bool] = FieldInfo(alias="isLargeValue", default=None)

    persistence_timestamp: Optional[int] = FieldInfo(alias="persistenceTimestamp", default=None)

    request_id: Optional[str] = FieldInfo(alias="requestId", default=None)
    """A unique ID associated with this request."""

    selected_by_user: Optional[bool] = FieldInfo(alias="selectedByUser", default=None)
    """Whether the value was selected by a user."""

    selected_by_user_timestamp: Optional[int] = FieldInfo(alias="selectedByUserTimestamp", default=None)
    """The timestamp when the value was selected by a user, if applicable."""

    source: Optional[
        Literal[
            "UNKNOWN",
            "IMPORT",
            "API",
            "FORM",
            "ANALYTICS",
            "MIGRATION",
            "SALESFORCE",
            "INTEGRATION",
            "CONTACTS_WEB",
            "WAL_INCREMENTAL",
            "TASK",
            "EMAIL",
            "WORKFLOWS",
            "CALCULATED",
            "SOCIAL",
            "BATCH_UPDATE",
            "SIGNALS",
            "BIDEN",
            "DEFAULT",
            "COMPANIES",
            "DEALS",
            "ASSISTS",
            "PRESENTATIONS",
            "TALLY",
            "SIDEKICK",
            "CRM_UI",
            "MERGE_CONTACTS",
            "PORTAL_USER_ASSOCIATOR",
            "INTEGRATIONS_PLATFORM",
            "BCC_TO_CRM",
            "FORWARD_TO_CRM",
            "ENGAGEMENTS",
            "SALES",
            "HEISENBERG",
            "LEADIN",
            "GMAIL_INTEGRATION",
            "ACADEMY",
            "SALES_MESSAGES",
            "AVATARS_SERVICE",
            "MERGE_COMPANIES",
            "SEQUENCES",
            "COMPANY_FAMILIES",
            "MOBILE_IOS",
            "MOBILE_ANDROID",
            "CONTACTS",
            "ASSOCIATIONS",
            "EXTENSION",
            "SUCCESS",
            "BOT",
            "INTEGRATIONS_SYNC",
            "AUTOMATION_PLATFORM",
            "CONVERSATIONS",
            "EMAIL_INTEGRATION",
            "CONTENT_MEMBERSHIP",
            "QUOTES",
            "BET_ASSIGNMENT",
            "QUOTAS",
            "BET_CRM_CONNECTOR",
            "MEETINGS",
            "MERGE_OBJECTS",
            "RECYCLING_BIN",
            "ADS",
            "AI_GROUP",
            "COMMUNICATOR",
            "SETTINGS",
            "PROPERTY_SETTINGS",
            "PIPELINE_SETTINGS",
            "COMPANY_INSIGHTS",
            "BEHAVIORAL_EVENTS",
            "PAYMENTS",
            "GOALS",
            "PORTAL_OBJECT_SYNC",
            "APPROVALS",
            "FILE_MANAGER",
            "MARKETPLACE",
            "INTERNAL_PROCESSING",
            "FORECASTING",
            "SLACK_INTEGRATION",
            "CRM_UI_BULK_ACTION",
            "WORKFLOW_CONTACT_DELETE_ACTION",
            "ACCEPTANCE_TEST",
            "PLAYBOOKS",
            "CHATSPOT",
            "FLYWHEEL_PRODUCT_DATA_SYNC",
            "HELP_DESK",
            "BILLING",
            "DATA_ENRICHMENT",
            "AUTOMATION_JOURNEY",
            "MICROAPPS",
            "INTENT",
            "PROSPECTING_AGENT",
            "CENTRAL_EXCHANGE_RATES",
            "HELP_DESK_AI",
            "CONVERSATIONAL_ENRICHMENT",
            "CRM_PROCESSES_PLATFORM",
            "CLONE_OBJECTS",
            "MARKET_SOURCING",
            "DATASET",
            "PROPERTY_RESTORE",
        ]
    ] = None
    """The origin of the property value, such as "IMPORT" or "API"."""

    source_id: Optional[str] = FieldInfo(alias="sourceId", default=None)
    """The ID of the property source indicating where it was created."""

    source_label: Optional[str] = FieldInfo(alias="sourceLabel", default=None)
    """A human-readable label."""

    source_metadata: Optional[str] = FieldInfo(alias="sourceMetadata", default=None)
    """Source metadata encoded as a base64 string. For example: `ZXhhbXBsZSBzdHJpbmc=`"""

    source_vid: Optional[List[int]] = FieldInfo(alias="sourceVid", default=None)
    """The unique identifier associated with the source."""

    timestamp: Optional[int] = None
    """When the value was set, as a 64-bit integer."""

    unit: Optional[str] = None
    """The unit of measurement or context for the value."""

    updated_by_user_id: Optional[int] = FieldInfo(alias="updatedByUserId", default=None)
    """The ID of the user who updated the property."""

    use_timestamp_as_persistence_timestamp: Optional[bool] = FieldInfo(
        alias="useTimestampAsPersistenceTimestamp", default=None
    )
