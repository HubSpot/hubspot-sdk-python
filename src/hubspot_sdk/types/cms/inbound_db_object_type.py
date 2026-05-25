# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .scope_mapping import ScopeMapping

__all__ = ["InboundDBObjectType"]


class InboundDBObjectType(BaseModel):
    id: int

    allows_sensitive_properties: bool = FieldInfo(alias="allowsSensitiveProperties")

    create_date_property_name: str = FieldInfo(alias="createDatePropertyName")

    default_search_property_names: List[str] = FieldInfo(alias="defaultSearchPropertyNames")

    deleted: bool

    fully_qualified_name: str = FieldInfo(alias="fullyQualifiedName")

    has_custom_properties: bool = FieldInfo(alias="hasCustomProperties")

    has_default_properties: bool = FieldInfo(alias="hasDefaultProperties")

    has_external_object_ids: bool = FieldInfo(alias="hasExternalObjectIds")

    has_owners: bool = FieldInfo(alias="hasOwners")

    has_pipelines: bool = FieldInfo(alias="hasPipelines")

    indexed_for_filters_and_reports: bool = FieldInfo(alias="indexedForFiltersAndReports")

    last_modified_property_name: str = FieldInfo(alias="lastModifiedPropertyName")

    meta_type: Literal[
        "CMS_HUBDB",
        "HUBSPOT",
        "HUBSPOT_EVENT",
        "INTEGRATION",
        "INTEGRATION_EVENT",
        "PORTAL_SPECIFIC",
        "PORTAL_SPECIFIC_EVENT",
        "WORK",
        "WORK_SUB",
    ] = FieldInfo(alias="metaType")

    meta_type_id: int = FieldInfo(alias="metaTypeId")

    name: str

    object_type_id: str = FieldInfo(alias="objectTypeId")

    object_type_id_string: str = FieldInfo(alias="objectTypeIdString")

    permissioning_type: Literal["ALL_OR_NONE", "DO_NOT_CHECK_PERMISSIONS", "EXPLICIT", "OWNER_BASED", "TEAM_BASED"] = (
        FieldInfo(alias="permissioningType")
    )

    pipeline_property_name: str = FieldInfo(alias="pipelinePropertyName")

    pipeline_stage_property_name: str = FieldInfo(alias="pipelineStagePropertyName")

    required_properties: List[str] = FieldInfo(alias="requiredProperties")

    restorable: bool

    scope_mappings: List[ScopeMapping] = FieldInfo(alias="scopeMappings")

    secondary_display_label_property_names: List[str] = FieldInfo(alias="secondaryDisplayLabelPropertyNames")

    access_scope_name: Optional[str] = FieldInfo(alias="accessScopeName", default=None)

    created_at: Optional[int] = FieldInfo(alias="createdAt", default=None)

    description: Optional[str] = None

    integration_app_id: Optional[int] = FieldInfo(alias="integrationAppId", default=None)

    janus_group: Optional[str] = FieldInfo(alias="janusGroup", default=None)

    owner_portal_id: Optional[int] = FieldInfo(alias="ownerPortalId", default=None)

    pipeline_close_date_property_name: Optional[str] = FieldInfo(alias="pipelineCloseDatePropertyName", default=None)

    pipeline_time_to_close_property_name: Optional[str] = FieldInfo(
        alias="pipelineTimeToClosePropertyName", default=None
    )

    plural_form: Optional[str] = FieldInfo(alias="pluralForm", default=None)

    primary_display_label_property_name: Optional[str] = FieldInfo(
        alias="primaryDisplayLabelPropertyName", default=None
    )

    read_scope_name: Optional[str] = FieldInfo(alias="readScopeName", default=None)

    singular_form: Optional[str] = FieldInfo(alias="singularForm", default=None)

    status: Optional[Literal["Deprecated", "In development", "Live"]] = None

    visibilities: Optional[
        List[Literal["Customer-facing", "Internal only", "Customer-facing UI", "Customer-facing public API"]]
    ] = None

    visibility: Optional[
        Literal["Customer-facing", "Customer-facing public API", "Customer-facing UI", "Internal only"]
    ] = None

    write_scope_name: Optional[str] = FieldInfo(alias="writeScopeName", default=None)
