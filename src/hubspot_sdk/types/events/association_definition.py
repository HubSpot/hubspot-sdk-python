# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["AssociationDefinition"]


class AssociationDefinition(BaseModel):
    """The definition of an association"""

    id: int
    """The unique ID of the associated object (e.g., a contact ID)."""

    allows_custom_labels: bool = FieldInfo(alias="allowsCustomLabels")
    """Whether custom labels can be used in the association."""

    cardinality: Literal["ONE_TO_MANY", "ONE_TO_ONE"]
    """
    The cardinality from the source object's perspective, either "ONE_TO_ONE" or
    "ONE_TO_MANY".
    """

    category: Literal["HUBSPOT_DEFINED", "INTEGRATOR_DEFINED", "USER_DEFINED", "WORK"]
    """The error category"""

    from_object_type_id: str = FieldInfo(alias="fromObjectTypeId")
    """The ID of the source object type (e.g., 0-1 for contacts)."""

    has_all_associated_objects: bool = FieldInfo(alias="hasAllAssociatedObjects")
    """Whether all potential linked objects are included in the association"""

    has_cascading_deletes: bool = FieldInfo(alias="hasCascadingDeletes")
    """
    Whether deletions in the association should cause cascading deletes to linked
    objects.
    """

    has_user_enforced_max_from_object_ids: bool = FieldInfo(alias="hasUserEnforcedMaxFromObjectIds")
    """Whether a user has set a limit for the number of source objects."""

    has_user_enforced_max_to_object_ids: bool = FieldInfo(alias="hasUserEnforcedMaxToObjectIds")
    """Whether a user has set a limit for the number of destination objects."""

    hidden: bool
    """Whether the association is hidden or not."""

    inverse_allows_custom_labels: bool = FieldInfo(alias="inverseAllowsCustomLabels")
    """Whether the reverse association can also support custom labels."""

    inverse_cardinality: Literal["ONE_TO_MANY", "ONE_TO_ONE"] = FieldInfo(alias="inverseCardinality")
    """
    The cardinality from the destination object's perspective, either "ONE_TO_ONE"
    or "ONE_TO_MANY".
    """

    inverse_has_all_associated_objects: bool = FieldInfo(alias="inverseHasAllAssociatedObjects")
    """Whether all potential reverse linked objects are included in the association."""

    inverse_id: int = FieldInfo(alias="inverseId")
    """The unique ID for the inverse side of the association."""

    inverse_name: str = FieldInfo(alias="inverseName")
    """The name used to describe the inverse relationship in this association"""

    is_default: bool = FieldInfo(alias="isDefault")

    is_inverse_primary: bool = FieldInfo(alias="isInversePrimary")
    """Whether the inverse association is considered primary."""

    is_primary: bool = FieldInfo(alias="isPrimary")
    """Whether the association is the primary link between the entities involved."""

    max_from_object_ids: int = FieldInfo(alias="maxFromObjectIds")
    """The maximum number of source object IDs allowed in the association."""

    max_to_object_ids: int = FieldInfo(alias="maxToObjectIds")
    """The maximum number of destination object IDs allowed in the association."""

    name: str
    """For labeled association types, the internal name of the association."""

    portal_unique_identifier: str = FieldInfo(alias="portalUniqueIdentifier")
    """A unique across-portal ID applied to the association."""

    read_only: bool = FieldInfo(alias="readOnly")

    to_object_type_id: str = FieldInfo(alias="toObjectTypeId")
    """The ID of the destination object type (e.g., 0-3 for deals)."""

    from_object_type: Optional[
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
    ] = FieldInfo(alias="fromObjectType", default=None)
    """The name of the source object type (e.g,. "DEAL" or "QUOTE")."""

    hidden_reason: Optional[Literal["DEFAULT", "INTERNAL", "USER_CONFIGURED"]] = FieldInfo(
        alias="hiddenReason", default=None
    )

    inverse_label: Optional[str] = FieldInfo(alias="inverseLabel", default=None)
    """The label used to describe the reverse relationship in an association."""

    label: Optional[str] = None
    """The label given to an association."""

    to_object_type: Optional[
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
    ] = FieldInfo(alias="toObjectType", default=None)
    """The name of the destination object type (e.g,. "DEAL" or "QUOTE")."""
