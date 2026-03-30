# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .object_type_id_proto import ObjectTypeIDProto
from ..shared.automation_actions_option import AutomationActionsOption

__all__ = ["Property"]


class Property(BaseModel):
    """A HubSpot property"""

    allowed_object_types: List[ObjectTypeIDProto] = FieldInfo(alias="allowedObjectTypes")
    """Object types permitted to use this property."""

    calculated: bool
    """Whether the property is a calculated field."""

    can_archive: bool = FieldInfo(alias="canArchive")

    can_restore: bool = FieldInfo(alias="canRestore")

    created_at: int = FieldInfo(alias="createdAt")
    """The timestamp when the property was created, in ISO 8601 format."""

    created_user_id: int = FieldInfo(alias="createdUserId")
    """The ID of the user who created the property."""

    currency_property_name: str = FieldInfo(alias="currencyPropertyName")
    """The name of the related currency property."""

    data_sensitivity: Literal["high", "none", "standard"] = FieldInfo(alias="dataSensitivity")
    """
    Indicates the sensitivity level of the property, such as "non_sensitive",
    "sensitive", or "highly_sensitive".
    """

    date_display_hint: Literal["absolute", "absolute_with_relative", "time_since", "time_until"] = FieldInfo(
        alias="dateDisplayHint"
    )

    deleted: bool
    """Whether the property has been deleted."""

    description: str
    """A summary of the property's purpose."""

    display_mode: Literal["all_unique_versions", "current_value"] = FieldInfo(alias="displayMode")
    """The mode in which the property is displayed.

    Can be: "current_value" or "all_unique_versions".
    """

    display_order: int = FieldInfo(alias="displayOrder")
    """The position of the item relative to others in the list."""

    enforce_multivalue_uniqueness: bool = FieldInfo(alias="enforceMultivalueUniqueness")

    external_options: bool = FieldInfo(alias="externalOptions")
    """Applicable only for enumeration type properties.

    Should be set to true with a 'referencedObjectType' of 'OWNER'. Otherwise false.
    """

    external_options_reference_type: str = FieldInfo(alias="externalOptionsReferenceType")
    """
    When externalOptions is true, indicates the property's option values will be
    populated from other systems (e.g., "OWNER" for the hubspot_owner_id property).
    """

    favorited: bool
    """Deprecated. Whether the property is marked as a favorite."""

    favorited_order: int = FieldInfo(alias="favoritedOrder")
    """Deprecated. The order position when marked as favorited."""

    field_type: str = FieldInfo(alias="fieldType")
    """Determines how the property will appear in HubSpot's UI or on a form.

    Learn more in the properties API guide.
    """

    form_field: bool = FieldInfo(alias="formField")
    """Whether the property can appear on forms."""

    from_user_id: int = FieldInfo(alias="fromUserId")
    """The ID of the user who last updated the property."""

    group_name: str = FieldInfo(alias="groupName")
    """The name of the group to which the property is assigned."""

    has_unique_value: bool = FieldInfo(alias="hasUniqueValue")
    """Whether the property is a unique identifier property."""

    hidden: bool
    """Whether or not the property will be hidden from the HubSpot UI.

    It's recommended that this be set to false for custom properties.
    """

    hubspot_defined: bool = FieldInfo(alias="hubspotDefined")
    """A boolean value set to true for HubSpot default properties."""

    is_customized_default: bool = FieldInfo(alias="isCustomizedDefault")
    """For default properties, whether the property has been customized.

    Equivalent to the 'isCustomizedDefault' field.
    """

    is_multi_valued: bool = FieldInfo(alias="isMultiValued")
    """Whether the property can contain multiple values."""

    is_partial: bool = FieldInfo(alias="isPartial")
    """For default properties, whether the property has been customized.

    Equivalent to the 'isCustomizedDefault' field.
    """

    label: str
    """The display label for the property."""

    mutable_definition_not_deletable: bool = FieldInfo(alias="mutableDefinitionNotDeletable")
    """Whether the property definition can be customized but not deleted."""

    name: str
    """The internal name for the property."""

    number_display_hint: Literal["currency", "duration", "formatted", "percentage", "probability", "unformatted"] = (
        FieldInfo(alias="numberDisplayHint")
    )
    """Hint for how a number property is displayed and validated in HubSpot's UI.

    Can be: "unformatted", "formatted", "currency", "percentage", "duration", or
    "probability".
    """

    options: List[AutomationActionsOption]
    """A list of valid options for the property.

    This field is required for enumerated properties.
    """

    options_are_mutable: bool = FieldInfo(alias="optionsAreMutable")
    """Whether options can be modified after creation."""

    option_sort_strategy: Literal["ALPHABETICAL", "DISPLAY_ORDER"] = FieldInfo(alias="optionSortStrategy")
    """Specifies how to sort property options.

    Can be either "DISPLAY_ORDER" to defer to the displayOrder field, or
    "ALPHABETICAL".
    """

    owning_app_id: int = FieldInfo(alias="owningAppId")

    portal_id: int = FieldInfo(alias="portalId")
    """The ID of the HubSpot account where the property is defined."""

    read_only_definition: bool = FieldInfo(alias="readOnlyDefinition")
    """Whether the property's description is read-only."""

    read_only_value: bool = FieldInfo(alias="readOnlyValue")
    """Indicates if the property's value is read-only."""

    referenced_object_type: Literal[
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
    ] = FieldInfo(alias="referencedObjectType")
    """Deprecated. Use externalOptionsReferenceType instead."""

    searchable_in_global_search: bool = FieldInfo(alias="searchableInGlobalSearch")
    """Whether the property is searchable globaly."""

    search_text_analysis_mode: Literal["NONE", "NOT_ANALYZED_TEXT"] = FieldInfo(alias="searchTextAnalysisMode")

    sensitive_data_categories: List[str] = FieldInfo(alias="sensitiveDataCategories")
    """
    When sensitiveData is true, lists the type of sensitive data contained in the
    property (e.g., "HIPAA").
    """

    show_currency_symbol: bool = FieldInfo(alias="showCurrencySymbol")
    """Whether to show the currency symbol in HubSpot's UI."""

    text_display_hint: Literal[
        "domain_name",
        "email",
        "ip_address",
        "multi_line",
        "phone_number",
        "physical_address",
        "postal_code",
        "unformatted_single_line",
    ] = FieldInfo(alias="textDisplayHint")
    """Hint for how the text is displayed and validated in HubSpot's UI.

    Can be: "unformatted_single_line", "multi_line", "email", "phone_number",
    "domain_name", "ip_address", "physical_address", or "postal_code".
    """

    type: Literal[
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
    """The data type of the property, such as string or number."""

    updated_at: int = FieldInfo(alias="updatedAt")
    """The timestamp when the property was last updated, in ISO 8601 format."""
