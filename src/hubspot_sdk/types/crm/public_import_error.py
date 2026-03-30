# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .import_row_core import ImportRowCore
from ..shared.property_value import PropertyValue

__all__ = ["PublicImportError"]


class PublicImportError(BaseModel):
    id: str
    """A unique, stable identifier for this specific error."""

    created_at: int = FieldInfo(alias="createdAt")
    """The epoch millisecond timestamp when this error was recorded."""

    error_type: Literal[
        "AMBIGUOUS_ENUMERATION_OPTION",
        "ASSOCIATION_LABEL_NOT_FOUND",
        "ASSOCIATION_LIMIT_EXCEEDED",
        "ASSOCIATION_RECORD_NOT_FOUND",
        "COLUMN_TOO_LARGE",
        "COULD_NOT_FIND_BUSINESS_UNIT",
        "COULD_NOT_FIND_OWNER",
        "COULD_NOT_PARSE_DATE",
        "COULD_NOT_PARSE_NUMBER",
        "COULD_NOT_PARSE_ROW",
        "COULD_NOT_PARSE_TERM",
        "CREATE_ONLY_IMPORT",
        "DUPLICATE_ALTERNATE_ID",
        "DUPLICATE_ASSOCIATION_ID",
        "DUPLICATE_EVENT",
        "DUPLICATE_OBJECT_ID",
        "DUPLICATE_RECORD_ID",
        "DUPLICATE_ROW_CONTENT",
        "DUPLICATE_UNIQUE_CREATION_KEY",
        "DUPLICATE_UNIQUE_PROPERTY_VALUE",
        "FAILED_TO_CREATE_ASSOCIATION",
        "FAILED_TO_FIND_RECORD_FOR_ASSOCIATIONS",
        "FAILED_TO_OPT_OUT_CONTACT",
        "FAILED_TO_PROCESS_OBJECT_WITH_EMPTY_PROPERTY_VALUES",
        "FAILED_VALIDATION",
        "FILE_NOT_FOUND",
        "GDPR_BLACKLISTED_EMAIL",
        "INCORRECT_NUMBER_OF_COLUMNS",
        "INVALID_ALTERNATE_ID",
        "INVALID_ASSOCIATION_IDENTIFIER",
        "INVALID_ASSOCIATION_KEY",
        "INVALID_COLUMN_CONFIGURATION",
        "INVALID_CUSTOM_PROPERTY_VALIDATION",
        "INVALID_DOMAIN",
        "INVALID_EMAIL",
        "INVALID_ENUM_FILE_ID_OR_URL",
        "INVALID_ENUMERATION_OPTION",
        "INVALID_EVENT",
        "INVALID_EVENT_TIMESTAMP",
        "INVALID_FILE_TYPE",
        "INVALID_NUMBER_SIZE",
        "INVALID_OBJECT_ID",
        "INVALID_PROPERTY_VALUE_FORMAT",
        "INVALID_RECORD_ID",
        "INVALID_REQUIRED_PROPERTY",
        "INVALID_SHEET_COUNT",
        "INVALID_SPREADSHEET",
        "LIMIT_EXCEEDED",
        "MANY_ERRORS_IN_ROW",
        "MISSING_EVENT_DEFINITION",
        "MISSING_EVENT_TIMESTAMP",
        "MISSING_OBJECT_DEFINITION",
        "MISSING_REQUIRED_PROPERTY",
        "MULTIPLE_COMPANIES_WITH_THIS_DOMAIN",
        "MULTIPLE_OWNERS_FOUND",
        "NO_OBJECT_ID_FROM_ASSOCIATION_IDENTIFIER",
        "OUTSIDE_VALID_TERM_RANGE",
        "OUTSIDE_VALID_TIME_RANGE",
        "PORTAL_WIDE_CUSTOM_OBJECT_LIMIT_EXCEEDED",
        "PROPERTY_DEFINITION_NOT_FOUND",
        "PROPERTY_VALUE_NOT_FOUND",
        "ROW_DATA_TOO_LARGE",
        "SECONDARY_EMAIL_WRITE_FAILURE",
        "UNKNOWN_ASSOCIATION_RECORD_ID",
        "UNKNOWN_BAD_REQUEST",
        "UNKNOWN_ERROR",
        "UPDATE_ONLY_IMPORT",
    ] = FieldInfo(alias="errorType")
    """The classification of what went wrong during import processing."""

    source_data: ImportRowCore = FieldInfo(alias="sourceData")

    error_message: Optional[str] = FieldInfo(alias="errorMessage", default=None)
    """A human-readable error message."""

    extra_context: Optional[str] = FieldInfo(alias="extraContext", default=None)
    """Additional human-readable context about the error."""

    invalid_property_value: Optional[PropertyValue] = FieldInfo(alias="invalidPropertyValue", default=None)
    """
    Represents a single custom property of a marketing event, storing its name,
    value, metadata (like source, timestamp, and sensitivity), and related audit
    information for tracking changes.
    """

    invalid_value: Optional[str] = FieldInfo(alias="invalidValue", default=None)
    """The raw string value from the import file that caused the validation failure."""

    invalid_value_to_display: Optional[str] = FieldInfo(alias="invalidValueToDisplay", default=None)
    """
    A convenience accessor that returns either the value from `invalidPropertyValue`
    or `invalidValue`, whichever is present (preferring the property value).
    """

    known_column_number: Optional[int] = FieldInfo(alias="knownColumnNumber", default=None)
    """The zero-based column index in the import file where the error occurred"""

    object_type: Optional[
        Literal[
            "ABANDONED_CART",
            "ACCEPTANCE_TEST",
            "AD",
            "AD_ACCOUNT",
            "AD_CAMPAIGN",
            "AD_GROUP",
            "AI_FORECAST",
            "ALL_PAGES",
            "APPROVAL",
            "APPROVAL_STEP",
            "ATTRIBUTION",
            "AUDIENCE",
            "AUTOMATION_JOURNEY",
            "AUTOMATION_PLATFORM_FLOW",
            "AUTOMATION_PLATFORM_FLOW_ACTION",
            "BET_ALERT",
            "BET_DELIVERABLE_SERVICE",
            "BLOG_LISTING_PAGE",
            "BLOG_POST",
            "CALL",
            "CAMPAIGN",
            "CAMPAIGN_BUDGET_ITEM",
            "CAMPAIGN_SPEND_ITEM",
            "CAMPAIGN_STEP",
            "CAMPAIGN_TEMPLATE",
            "CAMPAIGN_TEMPLATE_STEP",
            "CART",
            "CASE_STUDY",
            "CHATFLOW",
            "CLIP",
            "CMS_URL",
            "COMBO_EVENT_CONFIGURATION",
            "COMMERCE_PAYMENT",
            "COMMUNICATION",
            "COMPANY",
            "CONTACT",
            "CONTACT_CREATE_ATTRIBUTION",
            "CONTENT",
            "CONTENT_AUDIT",
            "CONTENT_AUDIT_PAGE",
            "CONVERSATION",
            "CONVERSATION_INBOX",
            "CONVERSATION_SESSION",
            "CRM_OBJECTS_DUMMY_TYPE",
            "CRM_PIPELINES_DUMMY_TYPE",
            "CTA",
            "CTA_VARIANT",
            "DATA_PRIVACY_CONSENT",
            "DATA_SYNC_STATE",
            "DEAL",
            "DEAL_CREATE_ATTRIBUTION",
            "DEAL_REGISTRATION",
            "DEAL_SPLIT",
            "DISCOUNT",
            "DISCOUNT_CODE",
            "DISCOUNT_TEMPLATE",
            "EMAIL",
            "ENGAGEMENT",
            "EXPORT",
            "EXTERNAL_WEB_URL",
            "FEE",
            "FEEDBACK_SUBMISSION",
            "FEEDBACK_SURVEY",
            "FILE_MANAGER_FILE",
            "FILE_MANAGER_FOLDER",
            "FOLDER",
            "FORECAST",
            "FORM",
            "FORM_SUBMISSION_INBOUNDDB",
            "GOAL_TARGET",
            "GOAL_TARGET_GROUP",
            "GOAL_TEMPLATE",
            "GSC_PROPERTY",
            "HUB",
            "IMPORT",
            "INVOICE",
            "KEYWORD",
            "KNOWLEDGE_ARTICLE",
            "LANDING_PAGE",
            "LEAD",
            "LINE_ITEM",
            "MARKETING_CALENDAR",
            "MARKETING_CAMPAIGN_UTM",
            "MARKETING_EMAIL",
            "MARKETING_EVENT",
            "MARKETING_EVENT_ATTENDANCE",
            "MARKETING_SMS",
            "MEDIA_BRIDGE",
            "MEETING_EVENT",
            "MIC",
            "NOTE",
            "OBJECT_LIST",
            "ORDER",
            "OWNER",
            "PARTNER_ACCOUNT",
            "PARTNER_CLIENT",
            "PARTNER_CLIENT_REVENUE",
            "PARTNER_SERVICE",
            "PAYMENT_LINK",
            "PAYMENT_SCHEDULE",
            "PAYMENT_SCHEDULE_INSTALLMENT",
            "PERMISSIONS_TESTING",
            "PLAYBOOK",
            "PLAYBOOK_QUESTION",
            "PLAYBOOK_SUBMISSION",
            "PLAYBOOK_SUBMISSION_ANSWER",
            "PLAYLIST",
            "PLAYLIST_FOLDER",
            "PODCAST_EPISODE",
            "PORTAL",
            "PORTAL_OBJECT_SYNC_MESSAGE",
            "POSTAL_MAIL",
            "PRIVACY_SCANNER_COOKIE",
            "PRODUCT",
            "PRODUCT_OR_FOLDER",
            "PROPERTY_INFO",
            "PROSPECTING_AGENT_CONTACT_ASSIGNMENT",
            "PUBLISHING_TASK",
            "QUARANTINED_SUBMISSION",
            "QUOTA",
            "QUOTE",
            "QUOTE_FIELD",
            "QUOTE_MODULE",
            "QUOTE_MODULE_FIELD",
            "QUOTE_TEMPLATE",
            "RESTORABLE_CRM_OBJECT",
            "ROSTER",
            "ROSTER_MEMBER",
            "SALES_DOCUMENT",
            "SALES_TASK",
            "SALES_WORKLOAD",
            "SALESFORCE_SYNC_ERROR",
            "SCHEDULING_PAGE",
            "SCHEMAS_BACKEND_TEST",
            "SCORE_CONFIGURATION",
            "SEQUENCE",
            "SEQUENCE_ENROLLMENT",
            "SEQUENCE_STEP",
            "SEQUENCE_STEP_ENROLLMENT",
            "SERVICE",
            "SITE_PAGE",
            "SNIPPET",
            "SOCIAL_BROADCAST",
            "SOCIAL_CHANNEL",
            "SOCIAL_POST",
            "SOCIAL_PROFILE",
            "SOX_PROTECTED_DUMMY_TYPE",
            "SOX_PROTECTED_TEST_TYPE",
            "SUBMISSION_TAG",
            "SUBSCRIPTION",
            "TASK",
            "TASK_TEMPLATE",
            "TAX",
            "TEMPLATE",
            "TICKET",
            "UNKNOWN",
            "UNSUBSCRIBE",
            "USER",
            "VIEW",
            "VIEW_BLOCK",
            "WEB_INTERACTIVE",
        ]
    ] = FieldInfo(alias="objectType", default=None)
    """The CRM object type affected by this error."""

    object_type_id: Optional[str] = FieldInfo(alias="objectTypeId", default=None)
    """The modern object type identifier for the CRM object affected by this error."""
