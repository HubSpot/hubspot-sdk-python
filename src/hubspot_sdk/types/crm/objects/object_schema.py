# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ...._models import BaseModel
from ...shared.property import Property
from ...shared.object_type_definition_labels import ObjectTypeDefinitionLabels

__all__ = ["ObjectSchema", "Association"]


class Association(BaseModel):
    id: int
    """The unique ID of the associated object (e.g., a contact ID)."""

    allows_custom_labels: bool = FieldInfo(alias="allowsCustomLabels")
    """Whether custom labels can be used in the association."""

    cardinality: Literal["ONE_TO_ONE", "ONE_TO_MANY"]
    """
    The cardinality from the source object's perspective, either "ONE_TO_ONE" or
    "ONE_TO_MANY".
    """

    category: Literal["HUBSPOT_DEFINED", "USER_DEFINED", "INTEGRATOR_DEFINED"]
    """The category of the association.

    Can be: "HUBSPOT_DEFINED", "USER_DEFINED", or "INTEGRATOR_DEFINED"
    """

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

    inverse_cardinality: Literal["ONE_TO_ONE", "ONE_TO_MANY"] = FieldInfo(alias="inverseCardinality")
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

    to_object_type_id: str = FieldInfo(alias="toObjectTypeId")
    """The ID of the destination object type (e.g., 0-3 for deals)."""

    from_object_type: Optional[
        Literal[
            "CONTACT",
            "COMPANY",
            "DEAL",
            "ENGAGEMENT",
            "TICKET",
            "OWNER",
            "PRODUCT",
            "LINE_ITEM",
            "BET_DELIVERABLE_SERVICE",
            "CONTENT",
            "CONVERSATION",
            "BET_ALERT",
            "PORTAL",
            "QUOTE",
            "FORM_SUBMISSION_INBOUNDDB",
            "QUOTA",
            "UNSUBSCRIBE",
            "COMMUNICATION",
            "FEEDBACK_SUBMISSION",
            "ATTRIBUTION",
            "SALESFORCE_SYNC_ERROR",
            "RESTORABLE_CRM_OBJECT",
            "HUB",
            "LANDING_PAGE",
            "PRODUCT_OR_FOLDER",
            "TASK",
            "FORM",
            "MARKETING_EMAIL",
            "AD_ACCOUNT",
            "AD_CAMPAIGN",
            "AD_GROUP",
            "AD",
            "KEYWORD",
            "CAMPAIGN",
            "SOCIAL_CHANNEL",
            "SOCIAL_POST",
            "SITE_PAGE",
            "BLOG_POST",
            "IMPORT",
            "EXPORT",
            "CTA",
            "TASK_TEMPLATE",
            "AUTOMATION_PLATFORM_FLOW",
            "OBJECT_LIST",
            "NOTE",
            "MEETING_EVENT",
            "CALL",
            "EMAIL",
            "PUBLISHING_TASK",
            "CONVERSATION_SESSION",
            "CONTACT_CREATE_ATTRIBUTION",
            "INVOICE",
            "MARKETING_EVENT",
            "CONVERSATION_INBOX",
            "CHATFLOW",
            "MEDIA_BRIDGE",
            "SEQUENCE",
            "SEQUENCE_STEP",
            "FORECAST",
            "SNIPPET",
            "TEMPLATE",
            "DEAL_CREATE_ATTRIBUTION",
            "QUOTE_TEMPLATE",
            "QUOTE_MODULE",
            "QUOTE_MODULE_FIELD",
            "QUOTE_FIELD",
            "SEQUENCE_ENROLLMENT",
            "SUBSCRIPTION",
            "ACCEPTANCE_TEST",
            "SOCIAL_BROADCAST",
            "DEAL_SPLIT",
            "DEAL_REGISTRATION",
            "GOAL_TARGET",
            "GOAL_TARGET_GROUP",
            "PORTAL_OBJECT_SYNC_MESSAGE",
            "FILE_MANAGER_FILE",
            "FILE_MANAGER_FOLDER",
            "SEQUENCE_STEP_ENROLLMENT",
            "APPROVAL",
            "APPROVAL_STEP",
            "CTA_VARIANT",
            "SALES_DOCUMENT",
            "DISCOUNT",
            "FEE",
            "TAX",
            "MARKETING_CALENDAR",
            "PERMISSIONS_TESTING",
            "PRIVACY_SCANNER_COOKIE",
            "DATA_SYNC_STATE",
            "WEB_INTERACTIVE",
            "PLAYBOOK",
            "FOLDER",
            "PLAYBOOK_QUESTION",
            "PLAYBOOK_SUBMISSION",
            "PLAYBOOK_SUBMISSION_ANSWER",
            "COMMERCE_PAYMENT",
            "GSC_PROPERTY",
            "SOX_PROTECTED_DUMMY_TYPE",
            "BLOG_LISTING_PAGE",
            "QUARANTINED_SUBMISSION",
            "PAYMENT_SCHEDULE",
            "PAYMENT_SCHEDULE_INSTALLMENT",
            "MARKETING_CAMPAIGN_UTM",
            "DISCOUNT_TEMPLATE",
            "DISCOUNT_CODE",
            "FEEDBACK_SURVEY",
            "CMS_URL",
            "SALES_TASK",
            "SALES_WORKLOAD",
            "USER",
            "POSTAL_MAIL",
            "SCHEMAS_BACKEND_TEST",
            "PAYMENT_LINK",
            "SUBMISSION_TAG",
            "CAMPAIGN_STEP",
            "SCHEDULING_PAGE",
            "SOX_PROTECTED_TEST_TYPE",
            "ORDER",
            "MARKETING_SMS",
            "PARTNER_ACCOUNT",
            "CAMPAIGN_TEMPLATE",
            "CAMPAIGN_TEMPLATE_STEP",
            "PLAYLIST",
            "CLIP",
            "CAMPAIGN_BUDGET_ITEM",
            "CAMPAIGN_SPEND_ITEM",
            "MIC",
            "CONTENT_AUDIT",
            "CONTENT_AUDIT_PAGE",
            "PLAYLIST_FOLDER",
            "LEAD",
            "ABANDONED_CART",
            "EXTERNAL_WEB_URL",
            "VIEW",
            "VIEW_BLOCK",
            "ROSTER",
            "CART",
            "AUTOMATION_PLATFORM_FLOW_ACTION",
            "SOCIAL_PROFILE",
            "PARTNER_CLIENT",
            "ROSTER_MEMBER",
            "MARKETING_EVENT_ATTENDANCE",
            "ALL_PAGES",
            "AI_FORECAST",
            "CRM_PIPELINES_DUMMY_TYPE",
            "KNOWLEDGE_ARTICLE",
            "PROPERTY_INFO",
            "DATA_PRIVACY_CONSENT",
            "GOAL_TEMPLATE",
            "SCORE_CONFIGURATION",
            "AUDIENCE",
            "PARTNER_CLIENT_REVENUE",
            "AUTOMATION_JOURNEY",
            "COMBO_EVENT_CONFIGURATION",
            "CRM_OBJECTS_DUMMY_TYPE",
            "CASE_STUDY",
            "SERVICE",
            "PODCAST_EPISODE",
            "PARTNER_SERVICE",
            "UNKNOWN",
        ]
    ] = FieldInfo(alias="fromObjectType", default=None)
    """The name of the source object type (e.g,. "DEAL" or "QUOTE")."""

    inverse_label: Optional[str] = FieldInfo(alias="inverseLabel", default=None)
    """The label used to describe the reverse relationship in an association."""

    label: Optional[str] = None
    """The label given to an association."""

    to_object_type: Optional[
        Literal[
            "CONTACT",
            "COMPANY",
            "DEAL",
            "ENGAGEMENT",
            "TICKET",
            "OWNER",
            "PRODUCT",
            "LINE_ITEM",
            "BET_DELIVERABLE_SERVICE",
            "CONTENT",
            "CONVERSATION",
            "BET_ALERT",
            "PORTAL",
            "QUOTE",
            "FORM_SUBMISSION_INBOUNDDB",
            "QUOTA",
            "UNSUBSCRIBE",
            "COMMUNICATION",
            "FEEDBACK_SUBMISSION",
            "ATTRIBUTION",
            "SALESFORCE_SYNC_ERROR",
            "RESTORABLE_CRM_OBJECT",
            "HUB",
            "LANDING_PAGE",
            "PRODUCT_OR_FOLDER",
            "TASK",
            "FORM",
            "MARKETING_EMAIL",
            "AD_ACCOUNT",
            "AD_CAMPAIGN",
            "AD_GROUP",
            "AD",
            "KEYWORD",
            "CAMPAIGN",
            "SOCIAL_CHANNEL",
            "SOCIAL_POST",
            "SITE_PAGE",
            "BLOG_POST",
            "IMPORT",
            "EXPORT",
            "CTA",
            "TASK_TEMPLATE",
            "AUTOMATION_PLATFORM_FLOW",
            "OBJECT_LIST",
            "NOTE",
            "MEETING_EVENT",
            "CALL",
            "EMAIL",
            "PUBLISHING_TASK",
            "CONVERSATION_SESSION",
            "CONTACT_CREATE_ATTRIBUTION",
            "INVOICE",
            "MARKETING_EVENT",
            "CONVERSATION_INBOX",
            "CHATFLOW",
            "MEDIA_BRIDGE",
            "SEQUENCE",
            "SEQUENCE_STEP",
            "FORECAST",
            "SNIPPET",
            "TEMPLATE",
            "DEAL_CREATE_ATTRIBUTION",
            "QUOTE_TEMPLATE",
            "QUOTE_MODULE",
            "QUOTE_MODULE_FIELD",
            "QUOTE_FIELD",
            "SEQUENCE_ENROLLMENT",
            "SUBSCRIPTION",
            "ACCEPTANCE_TEST",
            "SOCIAL_BROADCAST",
            "DEAL_SPLIT",
            "DEAL_REGISTRATION",
            "GOAL_TARGET",
            "GOAL_TARGET_GROUP",
            "PORTAL_OBJECT_SYNC_MESSAGE",
            "FILE_MANAGER_FILE",
            "FILE_MANAGER_FOLDER",
            "SEQUENCE_STEP_ENROLLMENT",
            "APPROVAL",
            "APPROVAL_STEP",
            "CTA_VARIANT",
            "SALES_DOCUMENT",
            "DISCOUNT",
            "FEE",
            "TAX",
            "MARKETING_CALENDAR",
            "PERMISSIONS_TESTING",
            "PRIVACY_SCANNER_COOKIE",
            "DATA_SYNC_STATE",
            "WEB_INTERACTIVE",
            "PLAYBOOK",
            "FOLDER",
            "PLAYBOOK_QUESTION",
            "PLAYBOOK_SUBMISSION",
            "PLAYBOOK_SUBMISSION_ANSWER",
            "COMMERCE_PAYMENT",
            "GSC_PROPERTY",
            "SOX_PROTECTED_DUMMY_TYPE",
            "BLOG_LISTING_PAGE",
            "QUARANTINED_SUBMISSION",
            "PAYMENT_SCHEDULE",
            "PAYMENT_SCHEDULE_INSTALLMENT",
            "MARKETING_CAMPAIGN_UTM",
            "DISCOUNT_TEMPLATE",
            "DISCOUNT_CODE",
            "FEEDBACK_SURVEY",
            "CMS_URL",
            "SALES_TASK",
            "SALES_WORKLOAD",
            "USER",
            "POSTAL_MAIL",
            "SCHEMAS_BACKEND_TEST",
            "PAYMENT_LINK",
            "SUBMISSION_TAG",
            "CAMPAIGN_STEP",
            "SCHEDULING_PAGE",
            "SOX_PROTECTED_TEST_TYPE",
            "ORDER",
            "MARKETING_SMS",
            "PARTNER_ACCOUNT",
            "CAMPAIGN_TEMPLATE",
            "CAMPAIGN_TEMPLATE_STEP",
            "PLAYLIST",
            "CLIP",
            "CAMPAIGN_BUDGET_ITEM",
            "CAMPAIGN_SPEND_ITEM",
            "MIC",
            "CONTENT_AUDIT",
            "CONTENT_AUDIT_PAGE",
            "PLAYLIST_FOLDER",
            "LEAD",
            "ABANDONED_CART",
            "EXTERNAL_WEB_URL",
            "VIEW",
            "VIEW_BLOCK",
            "ROSTER",
            "CART",
            "AUTOMATION_PLATFORM_FLOW_ACTION",
            "SOCIAL_PROFILE",
            "PARTNER_CLIENT",
            "ROSTER_MEMBER",
            "MARKETING_EVENT_ATTENDANCE",
            "ALL_PAGES",
            "AI_FORECAST",
            "CRM_PIPELINES_DUMMY_TYPE",
            "KNOWLEDGE_ARTICLE",
            "PROPERTY_INFO",
            "DATA_PRIVACY_CONSENT",
            "GOAL_TEMPLATE",
            "SCORE_CONFIGURATION",
            "AUDIENCE",
            "PARTNER_CLIENT_REVENUE",
            "AUTOMATION_JOURNEY",
            "COMBO_EVENT_CONFIGURATION",
            "CRM_OBJECTS_DUMMY_TYPE",
            "CASE_STUDY",
            "SERVICE",
            "PODCAST_EPISODE",
            "PARTNER_SERVICE",
            "UNKNOWN",
        ]
    ] = FieldInfo(alias="toObjectType", default=None)
    """The name of the destination object type (e.g,. "DEAL" or "QUOTE")."""


class ObjectSchema(BaseModel):
    id: str
    """A unique ID for this schema's object type.

    Will be defined as {meta-type}-{unique ID}.
    """

    associations: List[Association]
    """Associations defined for a given object type."""

    labels: ObjectTypeDefinitionLabels

    name: str
    """A unique name for the schema's object type."""

    properties: List[Property]
    """Properties defined for this object type."""

    required_properties: List[str] = FieldInfo(alias="requiredProperties")
    """
    The names of properties that should be **required** when creating an object of
    this type.
    """

    archived: Optional[bool] = None

    created_at: Optional[datetime] = FieldInfo(alias="createdAt", default=None)
    """When the object schema was created."""

    created_by_user_id: Optional[int] = FieldInfo(alias="createdByUserId", default=None)

    description: Optional[str] = None

    fully_qualified_name: Optional[str] = FieldInfo(alias="fullyQualifiedName", default=None)
    """An assigned unique ID for the object, including portal ID and object name."""

    object_type_id: Optional[str] = FieldInfo(alias="objectTypeId", default=None)

    primary_display_property: Optional[str] = FieldInfo(alias="primaryDisplayProperty", default=None)
    """The name of the primary property for this object.

    This will be displayed as primary on the HubSpot record page for this object
    type.
    """

    searchable_properties: Optional[List[str]] = FieldInfo(alias="searchableProperties", default=None)
    """
    Names of properties that will be indexed for this object type in by HubSpot's
    product search.
    """

    secondary_display_properties: Optional[List[str]] = FieldInfo(alias="secondaryDisplayProperties", default=None)
    """The names of secondary properties for this object.

    These will be displayed as secondary on the HubSpot record page for this object
    type.
    """

    updated_at: Optional[datetime] = FieldInfo(alias="updatedAt", default=None)
    """When the object schema was last updated."""

    updated_by_user_id: Optional[int] = FieldInfo(alias="updatedByUserId", default=None)
