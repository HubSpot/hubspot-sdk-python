# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from ..._utils import PropertyInfo
from .long_field_schema_param import LongFieldSchemaParam
from .array_field_schema_param import ArrayFieldSchemaParam
from .double_field_schema_param import DoubleFieldSchemaParam
from .object_field_schema_param import ObjectFieldSchemaParam
from .string_field_schema_param import StringFieldSchemaParam
from .boolean_field_schema_param import BooleanFieldSchemaParam
from .integer_field_schema_param import IntegerFieldSchemaParam
from ..shared_params.automation_actions_option import AutomationActionsOption

__all__ = ["FieldTypeDefinitionParam", "Schema"]

Schema: TypeAlias = Union[
    IntegerFieldSchemaParam,
    LongFieldSchemaParam,
    DoubleFieldSchemaParam,
    StringFieldSchemaParam,
    BooleanFieldSchemaParam,
    ArrayFieldSchemaParam,
    ObjectFieldSchemaParam,
]


class FieldTypeDefinitionParam(TypedDict, total=False):
    external_options: Required[Annotated[bool, PropertyInfo(alias="externalOptions")]]
    """Indicates whether the field's options are sourced externally."""

    name: Required[str]
    """The unique identifier for the field."""

    options: Required[Iterable[AutomationActionsOption]]

    schema: Required[Schema]
    """Defines the structure and constraints of the field."""

    type: Required[
        Literal[
            "bool",
            "currency_number",
            "date",
            "datetime",
            "enumeration",
            "json",
            "number",
            "object_coordinates",
            "phone_number",
            "string",
        ]
    ]
    """
    Specifies the data type of the field, with accepted values like bool, date,
    datetime, enumeration, json, number, object_coordinates, phone_number, string.
    """

    use_chirp: Required[Annotated[bool, PropertyInfo(alias="useChirp")]]
    """Specifies whether the field uses the Chirp feature."""

    description: str
    """A detailed explanation of the field's purpose and usage."""

    external_options_reference_type: Annotated[str, PropertyInfo(alias="externalOptionsReferenceType")]
    """Specifies the type of external reference for options."""

    field_type: Annotated[
        Literal[
            "booleancheckbox",
            "calculation_equation",
            "calculation_read_time",
            "calculation_rollup",
            "calculation_score",
            "checkbox",
            "date",
            "file",
            "html",
            "number",
            "phonenumber",
            "radio",
            "select",
            "text",
            "textarea",
            "unknown",
        ],
        PropertyInfo(alias="fieldType"),
    ]
    """
    Describes the field's type in the UI, with accepted values like booleancheckbox,
    calculation_equation, checkbox, date, file, html, number, phonenumber, radio,
    select, text, textarea, unknown.
    """

    help_text: Annotated[str, PropertyInfo(alias="helpText")]
    """Additional information or guidance about the field."""

    label: str
    """The user-friendly label for the field."""

    options_url: Annotated[str, PropertyInfo(alias="optionsUrl")]
    """A URL that provides options for the field."""

    referenced_object_type: Annotated[
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
        ],
        PropertyInfo(alias="referencedObjectType"),
    ]
    """
    Indicates the type of object that the field references, with accepted values
    like OWNER.
    """
