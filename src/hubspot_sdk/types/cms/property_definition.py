# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .extension_data import ExtensionData
from .definition_source import DefinitionSource
from .rollup_expression import RollupExpression
from .default_requirements import DefaultRequirements
from .media_bridge_property import MediaBridgeProperty
from .field_level_permission import FieldLevelPermission
from .lookup_association_spec import LookupAssociationSpec
from .external_options_meta_data import ExternalOptionsMetaData
from .property_definition_source import PropertyDefinitionSource

__all__ = ["PropertyDefinition"]


class PropertyDefinition(BaseModel):
    object_type_id: str = FieldInfo(alias="objectTypeId")

    property: MediaBridgeProperty
    """A HubSpot property"""

    calculation_expression: Optional[object] = FieldInfo(alias="calculationExpression", default=None)

    calculation_formula: Optional[str] = FieldInfo(alias="calculationFormula", default=None)

    definition_source: Optional[PropertyDefinitionSource] = FieldInfo(alias="definitionSource", default=None)

    extension_data: Optional[ExtensionData] = FieldInfo(alias="extensionData", default=None)

    external_options_meta_data: Optional[ExternalOptionsMetaData] = FieldInfo(
        alias="externalOptionsMetaData", default=None
    )

    fulcrum_portal_id: Optional[int] = FieldInfo(alias="fulcrumPortalId", default=None)

    fulcrum_timestamp: Optional[int] = FieldInfo(alias="fulcrumTimestamp", default=None)

    janus_group: Optional[str] = FieldInfo(alias="janusGroup", default=None)

    lookup_association_spec: Optional[LookupAssociationSpec] = FieldInfo(alias="lookupAssociationSpec", default=None)

    permission: Optional[FieldLevelPermission] = None

    property_definition_source: Optional[DefinitionSource] = FieldInfo(alias="propertyDefinitionSource", default=None)

    property_requirements: Optional[DefaultRequirements] = FieldInfo(alias="propertyRequirements", default=None)

    rollup_expression: Optional[RollupExpression] = FieldInfo(alias="rollupExpression", default=None)
