# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from ...._models import BaseModel
from ...shared.property import Property
from ...shared.association_spec import AssociationSpec

__all__ = [
    "IntegratorSettingCreateObjectDefinitionResponse",
    "CreatedObjects",
    "CreatedObjectsObjectType",
    "CreatedObjectsObjectTypeScopeMapping",
    "CreatedObjectsProperty",
    "CreatedObjectsPropertyCalculationExpression",
    "CreatedObjectsPropertyCalculationExpressionCmsMediabridgeConstantBoolean",
    "CreatedObjectsPropertyCalculationExpressionCmsMediabridgeConstantNumber",
    "CreatedObjectsPropertyCalculationExpressionCmsMediabridgeConstantString",
    "CreatedObjectsPropertyCalculationExpressionCmsMediabridgeBooleanPropertyVariable",
    "CreatedObjectsPropertyCalculationExpressionCmsMediabridgeStringPropertyVariable",
    "CreatedObjectsPropertyCalculationExpressionCmsMediabridgeNumberPropertyVariable",
    "CreatedObjectsPropertyCalculationExpressionCmsMediabridgeTimestampOfPropertyVariable",
    "CreatedObjectsPropertyCalculationExpressionCmsMediabridgeBooleanTargetPropertyVariable",
    "CreatedObjectsPropertyCalculationExpressionCmsMediabridgeStringTargetPropertyVariable",
    "CreatedObjectsPropertyCalculationExpressionCmsMediabridgeNumberTargetPropertyVariable",
    "CreatedObjectsPropertyCalculationExpressionCmsMediabridgeTimestampOfTargetPropertyVariable",
    "CreatedObjectsPropertyCalculationExpressionCmsMediabridgeAddNumbers",
    "CreatedObjectsPropertyCalculationExpressionCmsMediabridgeSubtractNumbers",
    "CreatedObjectsPropertyCalculationExpressionCmsMediabridgeMultiplyNumbers",
    "CreatedObjectsPropertyCalculationExpressionCmsMediabridgeDivideNumbers",
    "CreatedObjectsPropertyCalculationExpressionCmsMediabridgeRoundDownNumbers",
    "CreatedObjectsPropertyCalculationExpressionCmsMediabridgeRoundUpNumbers",
    "CreatedObjectsPropertyCalculationExpressionCmsMediabridgeRoundNearestNumbers",
    "CreatedObjectsPropertyCalculationExpressionCmsMediabridgeUpperCase",
    "CreatedObjectsPropertyCalculationExpressionCmsMediabridgeLowerCase",
    "CreatedObjectsPropertyCalculationExpressionCmsMediabridgeConcatStrings",
    "CreatedObjectsPropertyCalculationExpressionCmsMediabridgeContains",
    "CreatedObjectsPropertyCalculationExpressionCmsMediabridgeBeginsWith",
    "CreatedObjectsPropertyCalculationExpressionCmsMediabridgeNumberToString",
    "CreatedObjectsPropertyCalculationExpressionCmsMediabridgeParseNumber",
    "CreatedObjectsPropertyCalculationExpressionCmsMediabridgeFetchExchangeRate",
    "CreatedObjectsPropertyCalculationExpressionCmsMediabridgeFetchCurrencyDecimalPlaces",
    "CreatedObjectsPropertyCalculationExpressionCmsMediabridgeFetchSingleCurrencyPortalCurrency",
    "CreatedObjectsPropertyCalculationExpressionCmsMediabridgeDatedExchangeRate",
    "CreatedObjectsPropertyCalculationExpressionCmsMediabridgePipelineProbability",
    "CreatedObjectsPropertyCalculationExpressionCmsMediabridgeMaxNumbers",
    "CreatedObjectsPropertyCalculationExpressionCmsMediabridgeMinNumbers",
    "CreatedObjectsPropertyCalculationExpressionCmsMediabridgeLessThan",
    "CreatedObjectsPropertyCalculationExpressionCmsMediabridgeLessThanOrEqual",
    "CreatedObjectsPropertyCalculationExpressionCmsMediabridgeMoreThan",
    "CreatedObjectsPropertyCalculationExpressionCmsMediabridgeMoreThanOrEqual",
    "CreatedObjectsPropertyCalculationExpressionCmsMediabridgeNumberEquals",
    "CreatedObjectsPropertyCalculationExpressionCmsMediabridgeStringEquals",
    "CreatedObjectsPropertyCalculationExpressionCmsMediabridgeIsPipelineStageClosed",
    "CreatedObjectsPropertyCalculationExpressionCmsMediabridgeNot",
    "CreatedObjectsPropertyCalculationExpressionCmsMediabridgeDate",
    "CreatedObjectsPropertyCalculationExpressionCmsMediabridgeMonth",
    "CreatedObjectsPropertyCalculationExpressionCmsMediabridgeYear",
    "CreatedObjectsPropertyCalculationExpressionCmsMediabridgeNow",
    "CreatedObjectsPropertyCalculationExpressionCmsMediabridgeTimeBetween",
    "CreatedObjectsPropertyCalculationExpressionCmsMediabridgePeriodToMonths",
    "CreatedObjectsPropertyCalculationExpressionCmsMediabridgePeriodToWeeks",
    "CreatedObjectsPropertyCalculationExpressionCmsMediabridgeAnd",
    "CreatedObjectsPropertyCalculationExpressionCmsMediabridgeOr",
    "CreatedObjectsPropertyCalculationExpressionCmsMediabridgeXor",
    "CreatedObjectsPropertyCalculationExpressionCmsMediabridgeIfString",
    "CreatedObjectsPropertyCalculationExpressionCmsMediabridgeIfNumber",
    "CreatedObjectsPropertyCalculationExpressionCmsMediabridgeIfBoolean",
    "CreatedObjectsPropertyCalculationExpressionCmsMediabridgeIsPresent",
    "CreatedObjectsPropertyCalculationExpressionCmsMediabridgeHasEmailReply",
    "CreatedObjectsPropertyCalculationExpressionCmsMediabridgeHasPlainTextEmailReply",
    "CreatedObjectsPropertyCalculationExpressionCmsMediabridgeExtractMostRecentEmailReplyHTML",
    "CreatedObjectsPropertyCalculationExpressionCmsMediabridgeExtractMostRecentEmailReplyText",
    "CreatedObjectsPropertyCalculationExpressionCmsMediabridgeExtractMostRecentPlainTextEmailReply",
    "CreatedObjectsPropertyCalculationExpressionCmsMediabridgeSetContainsString",
    "CreatedObjectsPropertyCalculationExpressionCmsMediabridgeIsEngagementType",
    "CreatedObjectsPropertyCalculationExpressionCmsMediabridgeFormatFullName",
    "CreatedObjectsPropertyCalculationExpressionCmsMediabridgeAbsoluteValue",
    "CreatedObjectsPropertyCalculationExpressionCmsMediabridgeSquareRoot",
    "CreatedObjectsPropertyCalculationExpressionCmsMediabridgePower",
    "CreatedObjectsPropertyCalculationExpressionCmsMediabridgeSubstring",
    "CreatedObjectsPropertyCalculationExpressionCmsMediabridgeEuler",
    "CreatedObjectsPropertyCalculationExpressionCmsMediabridgeStringLength",
    "CreatedObjectsPropertyCalculationExpressionCmsMediabridgeAddTime",
    "CreatedObjectsPropertyCalculationExpressionCmsMediabridgeSubtractTime",
    "CreatedObjectsPropertyDefinitionSource",
    "CreatedObjectsPropertyExtensionData",
    "CreatedObjectsPropertyExtensionDataCaseChangeTestExtensionData",
    "CreatedObjectsPropertyExtensionDataOptionDecoratorsExtensionData",
    "CreatedObjectsPropertyExtensionDataOptionDecoratorsExtensionDataOptionDecorators",
    "CreatedObjectsPropertyExtensionDataRequiredPropertiesExtensionData",
    "CreatedObjectsPropertyExtensionDataSoftRequiredPropertiesExtensionData",
    "CreatedObjectsPropertyExternalOptionsMetaData",
    "CreatedObjectsPropertyExternalOptionsMetaDataFilter",
    "CreatedObjectsPropertyPermission",
    "CreatedObjectsPropertyPropertyDefinitionSource",
    "CreatedObjectsPropertyPropertyRequirements",
    "CreatedObjectsPropertyRollupExpression",
    "CreatedObjectsPropertyRollupExpressionConditionalExpression",
    "CreatedObjectsPropertyRollupExpressionConditionalExpressionCmsMediabridgeConstantBoolean",
    "CreatedObjectsPropertyRollupExpressionConditionalExpressionCmsMediabridgeConstantNumber",
    "CreatedObjectsPropertyRollupExpressionConditionalExpressionCmsMediabridgeConstantString",
    "CreatedObjectsPropertyRollupExpressionConditionalExpressionCmsMediabridgeBooleanPropertyVariable",
    "CreatedObjectsPropertyRollupExpressionConditionalExpressionCmsMediabridgeStringPropertyVariable",
    "CreatedObjectsPropertyRollupExpressionConditionalExpressionCmsMediabridgeNumberPropertyVariable",
    "CreatedObjectsPropertyRollupExpressionConditionalExpressionCmsMediabridgeTimestampOfPropertyVariable",
    "CreatedObjectsPropertyRollupExpressionConditionalExpressionCmsMediabridgeBooleanTargetPropertyVariable",
    "CreatedObjectsPropertyRollupExpressionConditionalExpressionCmsMediabridgeStringTargetPropertyVariable",
    "CreatedObjectsPropertyRollupExpressionConditionalExpressionCmsMediabridgeNumberTargetPropertyVariable",
    "CreatedObjectsPropertyRollupExpressionConditionalExpressionCmsMediabridgeTimestampOfTargetPropertyVariable",
    "CreatedObjectsPropertyRollupExpressionConditionalExpressionCmsMediabridgeAddNumbers",
    "CreatedObjectsPropertyRollupExpressionConditionalExpressionCmsMediabridgeSubtractNumbers",
    "CreatedObjectsPropertyRollupExpressionConditionalExpressionCmsMediabridgeMultiplyNumbers",
    "CreatedObjectsPropertyRollupExpressionConditionalExpressionCmsMediabridgeDivideNumbers",
    "CreatedObjectsPropertyRollupExpressionConditionalExpressionCmsMediabridgeRoundDownNumbers",
    "CreatedObjectsPropertyRollupExpressionConditionalExpressionCmsMediabridgeRoundUpNumbers",
    "CreatedObjectsPropertyRollupExpressionConditionalExpressionCmsMediabridgeRoundNearestNumbers",
    "CreatedObjectsPropertyRollupExpressionConditionalExpressionCmsMediabridgeUpperCase",
    "CreatedObjectsPropertyRollupExpressionConditionalExpressionCmsMediabridgeLowerCase",
    "CreatedObjectsPropertyRollupExpressionConditionalExpressionCmsMediabridgeConcatStrings",
    "CreatedObjectsPropertyRollupExpressionConditionalExpressionCmsMediabridgeContains",
    "CreatedObjectsPropertyRollupExpressionConditionalExpressionCmsMediabridgeBeginsWith",
    "CreatedObjectsPropertyRollupExpressionConditionalExpressionCmsMediabridgeNumberToString",
    "CreatedObjectsPropertyRollupExpressionConditionalExpressionCmsMediabridgeParseNumber",
    "CreatedObjectsPropertyRollupExpressionConditionalExpressionCmsMediabridgeFetchExchangeRate",
    "CreatedObjectsPropertyRollupExpressionConditionalExpressionCmsMediabridgeFetchCurrencyDecimalPlaces",
    "CreatedObjectsPropertyRollupExpressionConditionalExpressionCmsMediabridgeFetchSingleCurrencyPortalCurrency",
    "CreatedObjectsPropertyRollupExpressionConditionalExpressionCmsMediabridgeDatedExchangeRate",
    "CreatedObjectsPropertyRollupExpressionConditionalExpressionCmsMediabridgePipelineProbability",
    "CreatedObjectsPropertyRollupExpressionConditionalExpressionCmsMediabridgeMaxNumbers",
    "CreatedObjectsPropertyRollupExpressionConditionalExpressionCmsMediabridgeMinNumbers",
    "CreatedObjectsPropertyRollupExpressionConditionalExpressionCmsMediabridgeLessThan",
    "CreatedObjectsPropertyRollupExpressionConditionalExpressionCmsMediabridgeLessThanOrEqual",
    "CreatedObjectsPropertyRollupExpressionConditionalExpressionCmsMediabridgeMoreThan",
    "CreatedObjectsPropertyRollupExpressionConditionalExpressionCmsMediabridgeMoreThanOrEqual",
    "CreatedObjectsPropertyRollupExpressionConditionalExpressionCmsMediabridgeNumberEquals",
    "CreatedObjectsPropertyRollupExpressionConditionalExpressionCmsMediabridgeStringEquals",
    "CreatedObjectsPropertyRollupExpressionConditionalExpressionCmsMediabridgeIsPipelineStageClosed",
    "CreatedObjectsPropertyRollupExpressionConditionalExpressionCmsMediabridgeNot",
    "CreatedObjectsPropertyRollupExpressionConditionalExpressionCmsMediabridgeDate",
    "CreatedObjectsPropertyRollupExpressionConditionalExpressionCmsMediabridgeMonth",
    "CreatedObjectsPropertyRollupExpressionConditionalExpressionCmsMediabridgeYear",
    "CreatedObjectsPropertyRollupExpressionConditionalExpressionCmsMediabridgeNow",
    "CreatedObjectsPropertyRollupExpressionConditionalExpressionCmsMediabridgeTimeBetween",
    "CreatedObjectsPropertyRollupExpressionConditionalExpressionCmsMediabridgePeriodToMonths",
    "CreatedObjectsPropertyRollupExpressionConditionalExpressionCmsMediabridgePeriodToWeeks",
    "CreatedObjectsPropertyRollupExpressionConditionalExpressionCmsMediabridgeAnd",
    "CreatedObjectsPropertyRollupExpressionConditionalExpressionCmsMediabridgeOr",
    "CreatedObjectsPropertyRollupExpressionConditionalExpressionCmsMediabridgeXor",
    "CreatedObjectsPropertyRollupExpressionConditionalExpressionCmsMediabridgeIfString",
    "CreatedObjectsPropertyRollupExpressionConditionalExpressionCmsMediabridgeIfNumber",
    "CreatedObjectsPropertyRollupExpressionConditionalExpressionCmsMediabridgeIfBoolean",
    "CreatedObjectsPropertyRollupExpressionConditionalExpressionCmsMediabridgeIsPresent",
    "CreatedObjectsPropertyRollupExpressionConditionalExpressionCmsMediabridgeHasEmailReply",
    "CreatedObjectsPropertyRollupExpressionConditionalExpressionCmsMediabridgeHasPlainTextEmailReply",
    "CreatedObjectsPropertyRollupExpressionConditionalExpressionCmsMediabridgeExtractMostRecentEmailReplyHTML",
    "CreatedObjectsPropertyRollupExpressionConditionalExpressionCmsMediabridgeExtractMostRecentEmailReplyText",
    "CreatedObjectsPropertyRollupExpressionConditionalExpressionCmsMediabridgeExtractMostRecentPlainTextEmailReply",
    "CreatedObjectsPropertyRollupExpressionConditionalExpressionCmsMediabridgeSetContainsString",
    "CreatedObjectsPropertyRollupExpressionConditionalExpressionCmsMediabridgeIsEngagementType",
    "CreatedObjectsPropertyRollupExpressionConditionalExpressionCmsMediabridgeFormatFullName",
    "CreatedObjectsPropertyRollupExpressionConditionalExpressionCmsMediabridgeAbsoluteValue",
    "CreatedObjectsPropertyRollupExpressionConditionalExpressionCmsMediabridgeSquareRoot",
    "CreatedObjectsPropertyRollupExpressionConditionalExpressionCmsMediabridgePower",
    "CreatedObjectsPropertyRollupExpressionConditionalExpressionCmsMediabridgeSubstring",
    "CreatedObjectsPropertyRollupExpressionConditionalExpressionCmsMediabridgeEuler",
    "CreatedObjectsPropertyRollupExpressionConditionalExpressionCmsMediabridgeStringLength",
    "CreatedObjectsPropertyRollupExpressionConditionalExpressionCmsMediabridgeAddTime",
    "CreatedObjectsPropertyRollupExpressionConditionalExpressionCmsMediabridgeSubtractTime",
    "CreatedObjectsPropertyGroup",
]


class CreatedObjectsObjectTypeScopeMapping(BaseModel):
    access_level: str = FieldInfo(alias="accessLevel")

    request_action: str = FieldInfo(alias="requestAction")

    scope_name: str = FieldInfo(alias="scopeName")


class CreatedObjectsObjectType(BaseModel):
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
        "HUBSPOT",
        "INTEGRATION",
        "PORTAL_SPECIFIC",
        "CMS_HUBDB",
        "HUBSPOT_EVENT",
        "INTEGRATION_EVENT",
        "PORTAL_SPECIFIC_EVENT",
    ] = FieldInfo(alias="metaType")

    meta_type_id: int = FieldInfo(alias="metaTypeId")

    name: str

    object_type_id: str = FieldInfo(alias="objectTypeId")

    permissioning_type: str = FieldInfo(alias="permissioningType")

    pipeline_property_name: str = FieldInfo(alias="pipelinePropertyName")

    pipeline_stage_property_name: str = FieldInfo(alias="pipelineStagePropertyName")

    required_properties: List[str] = FieldInfo(alias="requiredProperties")

    restorable: bool

    scope_mappings: List[CreatedObjectsObjectTypeScopeMapping] = FieldInfo(alias="scopeMappings")

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

    status: Optional[str] = None

    visibility: Optional[str] = None

    write_scope_name: Optional[str] = FieldInfo(alias="writeScopeName", default=None)


class CreatedObjectsPropertyCalculationExpressionCmsMediabridgeConstantBoolean(BaseModel):
    operator: Literal["CONSTANT_BOOLEAN"]

    inputs: Optional[List[object]] = None

    property_name: Optional[str] = FieldInfo(alias="propertyName", default=None)

    value: Optional[bool] = None


class CreatedObjectsPropertyCalculationExpressionCmsMediabridgeConstantNumber(BaseModel):
    operator: Literal["CONSTANT_NUMBER"]

    inputs: Optional[List[object]] = None

    property_name: Optional[str] = FieldInfo(alias="propertyName", default=None)

    value: Optional[float] = None


class CreatedObjectsPropertyCalculationExpressionCmsMediabridgeConstantString(BaseModel):
    operator: Literal["CONSTANT_STRING"]

    inputs: Optional[List[object]] = None

    property_name: Optional[str] = FieldInfo(alias="propertyName", default=None)

    value: Optional[str] = None


class CreatedObjectsPropertyCalculationExpressionCmsMediabridgeBooleanPropertyVariable(BaseModel):
    operator: Literal["BOOLEAN_PROPERTY_VARIABLE"]

    inputs: Optional[List[object]] = None

    property_name: Optional[str] = FieldInfo(alias="propertyName", default=None)

    value: Optional[bool] = None


class CreatedObjectsPropertyCalculationExpressionCmsMediabridgeStringPropertyVariable(BaseModel):
    operator: Literal["STRING_PROPERTY_VARIABLE"]

    inputs: Optional[List[object]] = None

    property_name: Optional[str] = FieldInfo(alias="propertyName", default=None)

    value: Optional[str] = None


class CreatedObjectsPropertyCalculationExpressionCmsMediabridgeNumberPropertyVariable(BaseModel):
    operator: Literal["NUMBER_PROPERTY_VARIABLE"]

    inputs: Optional[List[object]] = None

    property_name: Optional[str] = FieldInfo(alias="propertyName", default=None)

    value: Optional[float] = None


class CreatedObjectsPropertyCalculationExpressionCmsMediabridgeTimestampOfPropertyVariable(BaseModel):
    operator: Literal["TIMESTAMP_OF_PROPERTY_VARIABLE"]

    inputs: Optional[List[object]] = None

    property_name: Optional[str] = FieldInfo(alias="propertyName", default=None)

    value: Optional[str] = None


class CreatedObjectsPropertyCalculationExpressionCmsMediabridgeBooleanTargetPropertyVariable(BaseModel):
    operator: Literal["BOOLEAN_TARGET_PROPERTY_VARIABLE"]

    inputs: Optional[List[object]] = None

    property_name: Optional[str] = FieldInfo(alias="propertyName", default=None)

    value: Optional[bool] = None


class CreatedObjectsPropertyCalculationExpressionCmsMediabridgeStringTargetPropertyVariable(BaseModel):
    operator: Literal["STRING_TARGET_PROPERTY_VARIABLE"]

    inputs: Optional[List[object]] = None

    property_name: Optional[str] = FieldInfo(alias="propertyName", default=None)

    value: Optional[str] = None


class CreatedObjectsPropertyCalculationExpressionCmsMediabridgeNumberTargetPropertyVariable(BaseModel):
    operator: Literal["NUMBER_TARGET_PROPERTY_VARIABLE"]

    inputs: Optional[List[object]] = None

    property_name: Optional[str] = FieldInfo(alias="propertyName", default=None)

    value: Optional[float] = None


class CreatedObjectsPropertyCalculationExpressionCmsMediabridgeTimestampOfTargetPropertyVariable(BaseModel):
    operator: Literal["TIMESTAMP_OF_TARGET_PROPERTY_VARIABLE"]

    inputs: Optional[List[object]] = None

    property_name: Optional[str] = FieldInfo(alias="propertyName", default=None)

    value: Optional[str] = None


class CreatedObjectsPropertyCalculationExpressionCmsMediabridgeAddNumbers(BaseModel):
    enclosed_in_parentheses: bool = FieldInfo(alias="enclosedInParentheses")

    operator: Literal["ADD_NUMBERS"]

    inputs: Optional[List[object]] = None

    property_name: Optional[str] = FieldInfo(alias="propertyName", default=None)

    value: Optional[float] = None


class CreatedObjectsPropertyCalculationExpressionCmsMediabridgeSubtractNumbers(BaseModel):
    enclosed_in_parentheses: bool = FieldInfo(alias="enclosedInParentheses")

    operator: Literal["SUBTRACT_NUMBERS"]

    inputs: Optional[List[object]] = None

    property_name: Optional[str] = FieldInfo(alias="propertyName", default=None)

    value: Optional[float] = None


class CreatedObjectsPropertyCalculationExpressionCmsMediabridgeMultiplyNumbers(BaseModel):
    enclosed_in_parentheses: bool = FieldInfo(alias="enclosedInParentheses")

    operator: Literal["MULTIPLY_NUMBERS"]

    inputs: Optional[List[object]] = None

    property_name: Optional[str] = FieldInfo(alias="propertyName", default=None)

    value: Optional[float] = None


class CreatedObjectsPropertyCalculationExpressionCmsMediabridgeDivideNumbers(BaseModel):
    enclosed_in_parentheses: bool = FieldInfo(alias="enclosedInParentheses")

    operator: Literal["DIVIDE_NUMBERS"]

    inputs: Optional[List[object]] = None

    property_name: Optional[str] = FieldInfo(alias="propertyName", default=None)

    value: Optional[float] = None


class CreatedObjectsPropertyCalculationExpressionCmsMediabridgeRoundDownNumbers(BaseModel):
    operator: Literal["ROUND_DOWN"]

    inputs: Optional[List[object]] = None

    property_name: Optional[str] = FieldInfo(alias="propertyName", default=None)

    value: Optional[float] = None


class CreatedObjectsPropertyCalculationExpressionCmsMediabridgeRoundUpNumbers(BaseModel):
    operator: Literal["ROUND_UP"]

    inputs: Optional[List[object]] = None

    property_name: Optional[str] = FieldInfo(alias="propertyName", default=None)

    value: Optional[float] = None


class CreatedObjectsPropertyCalculationExpressionCmsMediabridgeRoundNearestNumbers(BaseModel):
    operator: Literal["ROUND_NEAREST"]

    inputs: Optional[List[object]] = None

    property_name: Optional[str] = FieldInfo(alias="propertyName", default=None)

    value: Optional[float] = None


class CreatedObjectsPropertyCalculationExpressionCmsMediabridgeUpperCase(BaseModel):
    operator: Literal["UPPER_CASE"]

    inputs: Optional[List[object]] = None

    property_name: Optional[str] = FieldInfo(alias="propertyName", default=None)

    value: Optional[str] = None


class CreatedObjectsPropertyCalculationExpressionCmsMediabridgeLowerCase(BaseModel):
    operator: Literal["LOWER_CASE"]

    inputs: Optional[List[object]] = None

    property_name: Optional[str] = FieldInfo(alias="propertyName", default=None)

    value: Optional[str] = None


class CreatedObjectsPropertyCalculationExpressionCmsMediabridgeConcatStrings(BaseModel):
    operator: Literal["CONCAT_STRINGS"]

    inputs: Optional[List[object]] = None

    property_name: Optional[str] = FieldInfo(alias="propertyName", default=None)

    value: Optional[str] = None


class CreatedObjectsPropertyCalculationExpressionCmsMediabridgeContains(BaseModel):
    operator: Literal["CONTAINS"]

    string_to_check: object = FieldInfo(alias="stringToCheck")

    inputs: Optional[List[object]] = None

    property_name: Optional[str] = FieldInfo(alias="propertyName", default=None)

    value: Optional[bool] = None


class CreatedObjectsPropertyCalculationExpressionCmsMediabridgeBeginsWith(BaseModel):
    operator: Literal["BEGINS_WITH"]

    string_to_check: object = FieldInfo(alias="stringToCheck")

    inputs: Optional[List[object]] = None

    property_name: Optional[str] = FieldInfo(alias="propertyName", default=None)

    value: Optional[bool] = None


class CreatedObjectsPropertyCalculationExpressionCmsMediabridgeNumberToString(BaseModel):
    operator: Literal["NUMBER_TO_STRING"]

    inputs: Optional[List[object]] = None

    property_name: Optional[str] = FieldInfo(alias="propertyName", default=None)

    value: Optional[str] = None


class CreatedObjectsPropertyCalculationExpressionCmsMediabridgeParseNumber(BaseModel):
    operator: Literal["PARSE_NUMBER"]

    inputs: Optional[List[object]] = None

    property_name: Optional[str] = FieldInfo(alias="propertyName", default=None)

    value: Optional[float] = None


class CreatedObjectsPropertyCalculationExpressionCmsMediabridgeFetchExchangeRate(BaseModel):
    operator: Literal["FETCH_EXCHANGE_RATE"]

    inputs: Optional[List[object]] = None

    property_name: Optional[str] = FieldInfo(alias="propertyName", default=None)

    value: Optional[float] = None


class CreatedObjectsPropertyCalculationExpressionCmsMediabridgeFetchCurrencyDecimalPlaces(BaseModel):
    operator: Literal["FETCH_CURRENCY_DECIMAL_PLACES"]

    inputs: Optional[List[object]] = None

    property_name: Optional[str] = FieldInfo(alias="propertyName", default=None)

    value: Optional[float] = None


class CreatedObjectsPropertyCalculationExpressionCmsMediabridgeFetchSingleCurrencyPortalCurrency(BaseModel):
    operator: Literal["FETCH_SINGLE_CURRENCY_PORTAL_CURRENCY"]

    inputs: Optional[List[object]] = None

    property_name: Optional[str] = FieldInfo(alias="propertyName", default=None)

    value: Optional[str] = None


class CreatedObjectsPropertyCalculationExpressionCmsMediabridgeDatedExchangeRate(BaseModel):
    operator: Literal["DATED_EXCHANGE_RATE"]

    inputs: Optional[List[object]] = None

    property_name: Optional[str] = FieldInfo(alias="propertyName", default=None)

    value: Optional[float] = None


class CreatedObjectsPropertyCalculationExpressionCmsMediabridgePipelineProbability(BaseModel):
    operator: Literal["PIPELINE_PROBABILITY"]

    inputs: Optional[List[object]] = None

    property_name: Optional[str] = FieldInfo(alias="propertyName", default=None)

    value: Optional[float] = None


class CreatedObjectsPropertyCalculationExpressionCmsMediabridgeMaxNumbers(BaseModel):
    operator: Literal["MAX_NUMBERS"]

    inputs: Optional[List[object]] = None

    property_name: Optional[str] = FieldInfo(alias="propertyName", default=None)

    value: Optional[float] = None


class CreatedObjectsPropertyCalculationExpressionCmsMediabridgeMinNumbers(BaseModel):
    operator: Literal["MIN_NUMBERS"]

    inputs: Optional[List[object]] = None

    property_name: Optional[str] = FieldInfo(alias="propertyName", default=None)

    value: Optional[float] = None


class CreatedObjectsPropertyCalculationExpressionCmsMediabridgeLessThan(BaseModel):
    operator: Literal["LESS_THAN"]

    inputs: Optional[List[object]] = None

    property_name: Optional[str] = FieldInfo(alias="propertyName", default=None)

    value: Optional[bool] = None


class CreatedObjectsPropertyCalculationExpressionCmsMediabridgeLessThanOrEqual(BaseModel):
    operator: Literal["LESS_THAN_OR_EQUAL"]

    inputs: Optional[List[object]] = None

    property_name: Optional[str] = FieldInfo(alias="propertyName", default=None)

    value: Optional[bool] = None


class CreatedObjectsPropertyCalculationExpressionCmsMediabridgeMoreThan(BaseModel):
    operator: Literal["MORE_THAN"]

    inputs: Optional[List[object]] = None

    property_name: Optional[str] = FieldInfo(alias="propertyName", default=None)

    value: Optional[bool] = None


class CreatedObjectsPropertyCalculationExpressionCmsMediabridgeMoreThanOrEqual(BaseModel):
    operator: Literal["MORE_THAN_OR_EQUAL"]

    inputs: Optional[List[object]] = None

    property_name: Optional[str] = FieldInfo(alias="propertyName", default=None)

    value: Optional[bool] = None


class CreatedObjectsPropertyCalculationExpressionCmsMediabridgeNumberEquals(BaseModel):
    operator: Literal["NUMBER_EQUALS"]

    inputs: Optional[List[object]] = None

    property_name: Optional[str] = FieldInfo(alias="propertyName", default=None)

    value: Optional[bool] = None


class CreatedObjectsPropertyCalculationExpressionCmsMediabridgeStringEquals(BaseModel):
    operator: Literal["STRING_EQUALS"]

    inputs: Optional[List[object]] = None

    property_name: Optional[str] = FieldInfo(alias="propertyName", default=None)

    value: Optional[bool] = None


class CreatedObjectsPropertyCalculationExpressionCmsMediabridgeIsPipelineStageClosed(BaseModel):
    operator: Literal["IS_PIPELINE_STAGE_CLOSED"]

    inputs: Optional[List[object]] = None

    property_name: Optional[str] = FieldInfo(alias="propertyName", default=None)

    value: Optional[bool] = None


class CreatedObjectsPropertyCalculationExpressionCmsMediabridgeNot(BaseModel):
    operator: Literal["NOT"]

    inputs: Optional[List[object]] = None

    property_name: Optional[str] = FieldInfo(alias="propertyName", default=None)

    value: Optional[bool] = None


class CreatedObjectsPropertyCalculationExpressionCmsMediabridgeDate(BaseModel):
    operator: Literal["DATE"]

    inputs: Optional[List[object]] = None

    property_name: Optional[str] = FieldInfo(alias="propertyName", default=None)

    value: Optional[float] = None


class CreatedObjectsPropertyCalculationExpressionCmsMediabridgeMonth(BaseModel):
    operator: Literal["MONTH"]

    inputs: Optional[List[object]] = None

    property_name: Optional[str] = FieldInfo(alias="propertyName", default=None)

    value: Optional[float] = None


class CreatedObjectsPropertyCalculationExpressionCmsMediabridgeYear(BaseModel):
    operator: Literal["YEAR"]

    inputs: Optional[List[object]] = None

    property_name: Optional[str] = FieldInfo(alias="propertyName", default=None)

    value: Optional[float] = None


class CreatedObjectsPropertyCalculationExpressionCmsMediabridgeNow(BaseModel):
    operator: Literal["NOW"]

    inputs: Optional[List[object]] = None

    property_name: Optional[str] = FieldInfo(alias="propertyName", default=None)

    value: Optional[float] = None


class CreatedObjectsPropertyCalculationExpressionCmsMediabridgeTimeBetween(BaseModel):
    operator: Literal["TIME_BETWEEN"]

    inputs: Optional[List[object]] = None

    property_name: Optional[str] = FieldInfo(alias="propertyName", default=None)

    value: Optional[float] = None


class CreatedObjectsPropertyCalculationExpressionCmsMediabridgePeriodToMonths(BaseModel):
    operator: Literal["PERIOD_TO_MONTHS"]

    inputs: Optional[List[object]] = None

    property_name: Optional[str] = FieldInfo(alias="propertyName", default=None)

    value: Optional[float] = None


class CreatedObjectsPropertyCalculationExpressionCmsMediabridgePeriodToWeeks(BaseModel):
    operator: Literal["PERIOD_TO_WEEKS"]

    inputs: Optional[List[object]] = None

    property_name: Optional[str] = FieldInfo(alias="propertyName", default=None)

    value: Optional[float] = None


class CreatedObjectsPropertyCalculationExpressionCmsMediabridgeAnd(BaseModel):
    enclosed_in_parentheses: bool = FieldInfo(alias="enclosedInParentheses")

    operator: Literal["AND"]

    inputs: Optional[List[object]] = None

    property_name: Optional[str] = FieldInfo(alias="propertyName", default=None)

    value: Optional[bool] = None


class CreatedObjectsPropertyCalculationExpressionCmsMediabridgeOr(BaseModel):
    enclosed_in_parentheses: bool = FieldInfo(alias="enclosedInParentheses")

    operator: Literal["OR"]

    inputs: Optional[List[object]] = None

    property_name: Optional[str] = FieldInfo(alias="propertyName", default=None)

    value: Optional[bool] = None


class CreatedObjectsPropertyCalculationExpressionCmsMediabridgeXor(BaseModel):
    enclosed_in_parentheses: bool = FieldInfo(alias="enclosedInParentheses")

    operator: Literal["XOR"]

    inputs: Optional[List[object]] = None

    property_name: Optional[str] = FieldInfo(alias="propertyName", default=None)

    value: Optional[bool] = None


class CreatedObjectsPropertyCalculationExpressionCmsMediabridgeIfString(BaseModel):
    enclosed_in_parentheses: bool = FieldInfo(alias="enclosedInParentheses")

    if_expression: object = FieldInfo(alias="ifExpression")

    operator: Literal["IF_STRING"]

    else_expression: Optional[object] = FieldInfo(alias="elseExpression", default=None)

    inputs: Optional[List[object]] = None

    property_name: Optional[str] = FieldInfo(alias="propertyName", default=None)

    value: Optional[str] = None


class CreatedObjectsPropertyCalculationExpressionCmsMediabridgeIfNumber(BaseModel):
    enclosed_in_parentheses: bool = FieldInfo(alias="enclosedInParentheses")

    if_expression: object = FieldInfo(alias="ifExpression")

    operator: Literal["IF_NUMBER"]

    else_expression: Optional[object] = FieldInfo(alias="elseExpression", default=None)

    inputs: Optional[List[object]] = None

    property_name: Optional[str] = FieldInfo(alias="propertyName", default=None)

    value: Optional[float] = None


class CreatedObjectsPropertyCalculationExpressionCmsMediabridgeIfBoolean(BaseModel):
    enclosed_in_parentheses: bool = FieldInfo(alias="enclosedInParentheses")

    if_expression: object = FieldInfo(alias="ifExpression")

    operator: Literal["IF_BOOLEAN"]

    else_expression: Optional[object] = FieldInfo(alias="elseExpression", default=None)

    inputs: Optional[List[object]] = None

    property_name: Optional[str] = FieldInfo(alias="propertyName", default=None)

    value: Optional[bool] = None


class CreatedObjectsPropertyCalculationExpressionCmsMediabridgeIsPresent(BaseModel):
    expression_to_evaluate: object = FieldInfo(alias="expressionToEvaluate")

    operator: Literal["IS_PRESENT"]

    inputs: Optional[List[object]] = None

    property_name: Optional[str] = FieldInfo(alias="propertyName", default=None)

    value: Optional[bool] = None


class CreatedObjectsPropertyCalculationExpressionCmsMediabridgeHasEmailReply(BaseModel):
    operator: Literal["HAS_EMAIL_REPLY"]

    inputs: Optional[List[object]] = None

    property_name: Optional[str] = FieldInfo(alias="propertyName", default=None)

    value: Optional[bool] = None


class CreatedObjectsPropertyCalculationExpressionCmsMediabridgeHasPlainTextEmailReply(BaseModel):
    operator: Literal["HAS_PLAIN_TEXT_EMAIL_REPLY"]

    inputs: Optional[List[object]] = None

    property_name: Optional[str] = FieldInfo(alias="propertyName", default=None)

    value: Optional[bool] = None


class CreatedObjectsPropertyCalculationExpressionCmsMediabridgeExtractMostRecentEmailReplyHTML(BaseModel):
    operator: Literal["EXTRACT_MOST_RECENT_EMAIL_REPLY_HTML"]

    inputs: Optional[List[object]] = None

    property_name: Optional[str] = FieldInfo(alias="propertyName", default=None)

    value: Optional[str] = None


class CreatedObjectsPropertyCalculationExpressionCmsMediabridgeExtractMostRecentEmailReplyText(BaseModel):
    operator: Literal["EXTRACT_MOST_RECENT_EMAIL_REPLY_TEXT"]

    inputs: Optional[List[object]] = None

    property_name: Optional[str] = FieldInfo(alias="propertyName", default=None)

    value: Optional[str] = None


class CreatedObjectsPropertyCalculationExpressionCmsMediabridgeExtractMostRecentPlainTextEmailReply(BaseModel):
    operator: Literal["EXTRACT_MOST_RECENT_PLAIN_TEXT_EMAIL_REPLY"]

    inputs: Optional[List[object]] = None

    property_name: Optional[str] = FieldInfo(alias="propertyName", default=None)

    value: Optional[str] = None


class CreatedObjectsPropertyCalculationExpressionCmsMediabridgeSetContainsString(BaseModel):
    operator: Literal["SET_CONTAINS_STRING"]

    string_to_check: object = FieldInfo(alias="stringToCheck")

    inputs: Optional[List[object]] = None

    property_name: Optional[str] = FieldInfo(alias="propertyName", default=None)

    value: Optional[bool] = None


class CreatedObjectsPropertyCalculationExpressionCmsMediabridgeIsEngagementType(BaseModel):
    operator: Literal["IS_ENGAGEMENT_TYPE"]

    inputs: Optional[List[object]] = None

    property_name: Optional[str] = FieldInfo(alias="propertyName", default=None)

    value: Optional[bool] = None


class CreatedObjectsPropertyCalculationExpressionCmsMediabridgeFormatFullName(BaseModel):
    operator: Literal["FORMAT_FULL_NAME"]

    inputs: Optional[List[object]] = None

    property_name: Optional[str] = FieldInfo(alias="propertyName", default=None)

    value: Optional[str] = None


class CreatedObjectsPropertyCalculationExpressionCmsMediabridgeAbsoluteValue(BaseModel):
    operator: Literal["ABSOLUTE_VALUE"]

    inputs: Optional[List[object]] = None

    property_name: Optional[str] = FieldInfo(alias="propertyName", default=None)

    value: Optional[float] = None


class CreatedObjectsPropertyCalculationExpressionCmsMediabridgeSquareRoot(BaseModel):
    operator: Literal["SQUARE_ROOT"]

    inputs: Optional[List[object]] = None

    property_name: Optional[str] = FieldInfo(alias="propertyName", default=None)

    value: Optional[float] = None


class CreatedObjectsPropertyCalculationExpressionCmsMediabridgePower(BaseModel):
    operator: Literal["POWER"]

    inputs: Optional[List[object]] = None

    property_name: Optional[str] = FieldInfo(alias="propertyName", default=None)

    value: Optional[float] = None


class CreatedObjectsPropertyCalculationExpressionCmsMediabridgeSubstring(BaseModel):
    operator: Literal["SUBSTRING"]

    string_to_check: object = FieldInfo(alias="stringToCheck")

    inputs: Optional[List[object]] = None

    property_name: Optional[str] = FieldInfo(alias="propertyName", default=None)

    value: Optional[str] = None


class CreatedObjectsPropertyCalculationExpressionCmsMediabridgeEuler(BaseModel):
    operator: Literal["EULER"]

    inputs: Optional[List[object]] = None

    property_name: Optional[str] = FieldInfo(alias="propertyName", default=None)

    value: Optional[float] = None


class CreatedObjectsPropertyCalculationExpressionCmsMediabridgeStringLength(BaseModel):
    operator: Literal["STRING_LENGTH"]

    inputs: Optional[List[object]] = None

    property_name: Optional[str] = FieldInfo(alias="propertyName", default=None)

    value: Optional[float] = None


class CreatedObjectsPropertyCalculationExpressionCmsMediabridgeAddTime(BaseModel):
    operator: Literal["ADD_TIME"]

    string_to_check: object = FieldInfo(alias="stringToCheck")

    inputs: Optional[List[object]] = None

    property_name: Optional[str] = FieldInfo(alias="propertyName", default=None)

    value: Optional[float] = None


class CreatedObjectsPropertyCalculationExpressionCmsMediabridgeSubtractTime(BaseModel):
    operator: Literal["SUBTRACT_TIME"]

    string_to_check: object = FieldInfo(alias="stringToCheck")

    inputs: Optional[List[object]] = None

    property_name: Optional[str] = FieldInfo(alias="propertyName", default=None)

    value: Optional[float] = None


CreatedObjectsPropertyCalculationExpression: TypeAlias = Union[
    CreatedObjectsPropertyCalculationExpressionCmsMediabridgeConstantBoolean,
    CreatedObjectsPropertyCalculationExpressionCmsMediabridgeConstantNumber,
    CreatedObjectsPropertyCalculationExpressionCmsMediabridgeConstantString,
    CreatedObjectsPropertyCalculationExpressionCmsMediabridgeBooleanPropertyVariable,
    CreatedObjectsPropertyCalculationExpressionCmsMediabridgeStringPropertyVariable,
    CreatedObjectsPropertyCalculationExpressionCmsMediabridgeNumberPropertyVariable,
    CreatedObjectsPropertyCalculationExpressionCmsMediabridgeTimestampOfPropertyVariable,
    CreatedObjectsPropertyCalculationExpressionCmsMediabridgeBooleanTargetPropertyVariable,
    CreatedObjectsPropertyCalculationExpressionCmsMediabridgeStringTargetPropertyVariable,
    CreatedObjectsPropertyCalculationExpressionCmsMediabridgeNumberTargetPropertyVariable,
    CreatedObjectsPropertyCalculationExpressionCmsMediabridgeTimestampOfTargetPropertyVariable,
    CreatedObjectsPropertyCalculationExpressionCmsMediabridgeAddNumbers,
    CreatedObjectsPropertyCalculationExpressionCmsMediabridgeSubtractNumbers,
    CreatedObjectsPropertyCalculationExpressionCmsMediabridgeMultiplyNumbers,
    CreatedObjectsPropertyCalculationExpressionCmsMediabridgeDivideNumbers,
    CreatedObjectsPropertyCalculationExpressionCmsMediabridgeRoundDownNumbers,
    CreatedObjectsPropertyCalculationExpressionCmsMediabridgeRoundUpNumbers,
    CreatedObjectsPropertyCalculationExpressionCmsMediabridgeRoundNearestNumbers,
    CreatedObjectsPropertyCalculationExpressionCmsMediabridgeUpperCase,
    CreatedObjectsPropertyCalculationExpressionCmsMediabridgeLowerCase,
    CreatedObjectsPropertyCalculationExpressionCmsMediabridgeConcatStrings,
    CreatedObjectsPropertyCalculationExpressionCmsMediabridgeContains,
    CreatedObjectsPropertyCalculationExpressionCmsMediabridgeBeginsWith,
    CreatedObjectsPropertyCalculationExpressionCmsMediabridgeNumberToString,
    CreatedObjectsPropertyCalculationExpressionCmsMediabridgeParseNumber,
    CreatedObjectsPropertyCalculationExpressionCmsMediabridgeFetchExchangeRate,
    CreatedObjectsPropertyCalculationExpressionCmsMediabridgeFetchCurrencyDecimalPlaces,
    CreatedObjectsPropertyCalculationExpressionCmsMediabridgeFetchSingleCurrencyPortalCurrency,
    CreatedObjectsPropertyCalculationExpressionCmsMediabridgeDatedExchangeRate,
    CreatedObjectsPropertyCalculationExpressionCmsMediabridgePipelineProbability,
    CreatedObjectsPropertyCalculationExpressionCmsMediabridgeMaxNumbers,
    CreatedObjectsPropertyCalculationExpressionCmsMediabridgeMinNumbers,
    CreatedObjectsPropertyCalculationExpressionCmsMediabridgeLessThan,
    CreatedObjectsPropertyCalculationExpressionCmsMediabridgeLessThanOrEqual,
    CreatedObjectsPropertyCalculationExpressionCmsMediabridgeMoreThan,
    CreatedObjectsPropertyCalculationExpressionCmsMediabridgeMoreThanOrEqual,
    CreatedObjectsPropertyCalculationExpressionCmsMediabridgeNumberEquals,
    CreatedObjectsPropertyCalculationExpressionCmsMediabridgeStringEquals,
    CreatedObjectsPropertyCalculationExpressionCmsMediabridgeIsPipelineStageClosed,
    CreatedObjectsPropertyCalculationExpressionCmsMediabridgeNot,
    CreatedObjectsPropertyCalculationExpressionCmsMediabridgeDate,
    CreatedObjectsPropertyCalculationExpressionCmsMediabridgeMonth,
    CreatedObjectsPropertyCalculationExpressionCmsMediabridgeYear,
    CreatedObjectsPropertyCalculationExpressionCmsMediabridgeNow,
    CreatedObjectsPropertyCalculationExpressionCmsMediabridgeTimeBetween,
    CreatedObjectsPropertyCalculationExpressionCmsMediabridgePeriodToMonths,
    CreatedObjectsPropertyCalculationExpressionCmsMediabridgePeriodToWeeks,
    CreatedObjectsPropertyCalculationExpressionCmsMediabridgeAnd,
    CreatedObjectsPropertyCalculationExpressionCmsMediabridgeOr,
    CreatedObjectsPropertyCalculationExpressionCmsMediabridgeXor,
    CreatedObjectsPropertyCalculationExpressionCmsMediabridgeIfString,
    CreatedObjectsPropertyCalculationExpressionCmsMediabridgeIfNumber,
    CreatedObjectsPropertyCalculationExpressionCmsMediabridgeIfBoolean,
    CreatedObjectsPropertyCalculationExpressionCmsMediabridgeIsPresent,
    CreatedObjectsPropertyCalculationExpressionCmsMediabridgeHasEmailReply,
    CreatedObjectsPropertyCalculationExpressionCmsMediabridgeHasPlainTextEmailReply,
    CreatedObjectsPropertyCalculationExpressionCmsMediabridgeExtractMostRecentEmailReplyHTML,
    CreatedObjectsPropertyCalculationExpressionCmsMediabridgeExtractMostRecentEmailReplyText,
    CreatedObjectsPropertyCalculationExpressionCmsMediabridgeExtractMostRecentPlainTextEmailReply,
    CreatedObjectsPropertyCalculationExpressionCmsMediabridgeSetContainsString,
    CreatedObjectsPropertyCalculationExpressionCmsMediabridgeIsEngagementType,
    CreatedObjectsPropertyCalculationExpressionCmsMediabridgeFormatFullName,
    CreatedObjectsPropertyCalculationExpressionCmsMediabridgeAbsoluteValue,
    CreatedObjectsPropertyCalculationExpressionCmsMediabridgeSquareRoot,
    CreatedObjectsPropertyCalculationExpressionCmsMediabridgePower,
    CreatedObjectsPropertyCalculationExpressionCmsMediabridgeSubstring,
    CreatedObjectsPropertyCalculationExpressionCmsMediabridgeEuler,
    CreatedObjectsPropertyCalculationExpressionCmsMediabridgeStringLength,
    CreatedObjectsPropertyCalculationExpressionCmsMediabridgeAddTime,
    CreatedObjectsPropertyCalculationExpressionCmsMediabridgeSubtractTime,
]


class CreatedObjectsPropertyDefinitionSource(BaseModel):
    type: Literal["GLOBAL", "OBJECT_TYPE", "HAVEN_BRANCH", "PORTAL"]

    name: Optional[str] = None


class CreatedObjectsPropertyExtensionDataCaseChangeTestExtensionData(BaseModel):
    mood: str


class CreatedObjectsPropertyExtensionDataOptionDecoratorsExtensionDataOptionDecorators(BaseModel):
    color: str


class CreatedObjectsPropertyExtensionDataOptionDecoratorsExtensionData(BaseModel):
    option_decorators: Dict[str, CreatedObjectsPropertyExtensionDataOptionDecoratorsExtensionDataOptionDecorators] = (
        FieldInfo(alias="optionDecorators")
    )

    option_decorator_style: str = FieldInfo(alias="optionDecoratorStyle")


class CreatedObjectsPropertyExtensionDataRequiredPropertiesExtensionData(BaseModel):
    is_required_property: bool = FieldInfo(alias="isRequiredProperty")


class CreatedObjectsPropertyExtensionDataSoftRequiredPropertiesExtensionData(BaseModel):
    is_soft_required_property: bool = FieldInfo(alias="isSoftRequiredProperty")


class CreatedObjectsPropertyExtensionData(BaseModel):
    extension_status_map: Dict[str, str] = FieldInfo(alias="extensionStatusMap")

    tags: List[str]

    case_change_test_extension_data: Optional[CreatedObjectsPropertyExtensionDataCaseChangeTestExtensionData] = (
        FieldInfo(alias="caseChangeTestExtensionData", default=None)
    )

    option_decorators_extension_data: Optional[CreatedObjectsPropertyExtensionDataOptionDecoratorsExtensionData] = (
        FieldInfo(alias="optionDecoratorsExtensionData", default=None)
    )

    required_properties_extension_data: Optional[CreatedObjectsPropertyExtensionDataRequiredPropertiesExtensionData] = (
        FieldInfo(alias="requiredPropertiesExtensionData", default=None)
    )

    soft_required_properties_extension_data: Optional[
        CreatedObjectsPropertyExtensionDataSoftRequiredPropertiesExtensionData
    ] = FieldInfo(alias="softRequiredPropertiesExtensionData", default=None)


class CreatedObjectsPropertyExternalOptionsMetaDataFilter(BaseModel):
    include_unconfirmed_users: bool = FieldInfo(alias="includeUnconfirmedUsers")

    pipeline_ids: List[str] = FieldInfo(alias="pipelineIds")


class CreatedObjectsPropertyExternalOptionsMetaData(BaseModel):
    filter: Optional[CreatedObjectsPropertyExternalOptionsMetaDataFilter] = None

    related_object_type_id: Optional[str] = FieldInfo(alias="relatedObjectTypeId", default=None)


class CreatedObjectsPropertyPermission(BaseModel):
    access_level: str = FieldInfo(alias="accessLevel")


class CreatedObjectsPropertyPropertyDefinitionSource(BaseModel):
    type: str

    name: Optional[str] = None


class CreatedObjectsPropertyPropertyRequirements(BaseModel):
    gates: List[str]

    operator: Literal["AND", "OR"]

    scope_names: List[str] = FieldInfo(alias="scopeNames")

    settings: List[str]


class CreatedObjectsPropertyRollupExpressionConditionalExpressionCmsMediabridgeConstantBoolean(BaseModel):
    operator: Literal["CONSTANT_BOOLEAN"]

    inputs: Optional[List[object]] = None

    property_name: Optional[str] = FieldInfo(alias="propertyName", default=None)

    value: Optional[bool] = None


class CreatedObjectsPropertyRollupExpressionConditionalExpressionCmsMediabridgeConstantNumber(BaseModel):
    operator: Literal["CONSTANT_NUMBER"]

    inputs: Optional[List[object]] = None

    property_name: Optional[str] = FieldInfo(alias="propertyName", default=None)

    value: Optional[float] = None


class CreatedObjectsPropertyRollupExpressionConditionalExpressionCmsMediabridgeConstantString(BaseModel):
    operator: Literal["CONSTANT_STRING"]

    inputs: Optional[List[object]] = None

    property_name: Optional[str] = FieldInfo(alias="propertyName", default=None)

    value: Optional[str] = None


class CreatedObjectsPropertyRollupExpressionConditionalExpressionCmsMediabridgeBooleanPropertyVariable(BaseModel):
    operator: Literal["BOOLEAN_PROPERTY_VARIABLE"]

    inputs: Optional[List[object]] = None

    property_name: Optional[str] = FieldInfo(alias="propertyName", default=None)

    value: Optional[bool] = None


class CreatedObjectsPropertyRollupExpressionConditionalExpressionCmsMediabridgeStringPropertyVariable(BaseModel):
    operator: Literal["STRING_PROPERTY_VARIABLE"]

    inputs: Optional[List[object]] = None

    property_name: Optional[str] = FieldInfo(alias="propertyName", default=None)

    value: Optional[str] = None


class CreatedObjectsPropertyRollupExpressionConditionalExpressionCmsMediabridgeNumberPropertyVariable(BaseModel):
    operator: Literal["NUMBER_PROPERTY_VARIABLE"]

    inputs: Optional[List[object]] = None

    property_name: Optional[str] = FieldInfo(alias="propertyName", default=None)

    value: Optional[float] = None


class CreatedObjectsPropertyRollupExpressionConditionalExpressionCmsMediabridgeTimestampOfPropertyVariable(BaseModel):
    operator: Literal["TIMESTAMP_OF_PROPERTY_VARIABLE"]

    inputs: Optional[List[object]] = None

    property_name: Optional[str] = FieldInfo(alias="propertyName", default=None)

    value: Optional[str] = None


class CreatedObjectsPropertyRollupExpressionConditionalExpressionCmsMediabridgeBooleanTargetPropertyVariable(BaseModel):
    operator: Literal["BOOLEAN_TARGET_PROPERTY_VARIABLE"]

    inputs: Optional[List[object]] = None

    property_name: Optional[str] = FieldInfo(alias="propertyName", default=None)

    value: Optional[bool] = None


class CreatedObjectsPropertyRollupExpressionConditionalExpressionCmsMediabridgeStringTargetPropertyVariable(BaseModel):
    operator: Literal["STRING_TARGET_PROPERTY_VARIABLE"]

    inputs: Optional[List[object]] = None

    property_name: Optional[str] = FieldInfo(alias="propertyName", default=None)

    value: Optional[str] = None


class CreatedObjectsPropertyRollupExpressionConditionalExpressionCmsMediabridgeNumberTargetPropertyVariable(BaseModel):
    operator: Literal["NUMBER_TARGET_PROPERTY_VARIABLE"]

    inputs: Optional[List[object]] = None

    property_name: Optional[str] = FieldInfo(alias="propertyName", default=None)

    value: Optional[float] = None


class CreatedObjectsPropertyRollupExpressionConditionalExpressionCmsMediabridgeTimestampOfTargetPropertyVariable(
    BaseModel
):
    operator: Literal["TIMESTAMP_OF_TARGET_PROPERTY_VARIABLE"]

    inputs: Optional[List[object]] = None

    property_name: Optional[str] = FieldInfo(alias="propertyName", default=None)

    value: Optional[str] = None


class CreatedObjectsPropertyRollupExpressionConditionalExpressionCmsMediabridgeAddNumbers(BaseModel):
    enclosed_in_parentheses: bool = FieldInfo(alias="enclosedInParentheses")

    operator: Literal["ADD_NUMBERS"]

    inputs: Optional[List[object]] = None

    property_name: Optional[str] = FieldInfo(alias="propertyName", default=None)

    value: Optional[float] = None


class CreatedObjectsPropertyRollupExpressionConditionalExpressionCmsMediabridgeSubtractNumbers(BaseModel):
    enclosed_in_parentheses: bool = FieldInfo(alias="enclosedInParentheses")

    operator: Literal["SUBTRACT_NUMBERS"]

    inputs: Optional[List[object]] = None

    property_name: Optional[str] = FieldInfo(alias="propertyName", default=None)

    value: Optional[float] = None


class CreatedObjectsPropertyRollupExpressionConditionalExpressionCmsMediabridgeMultiplyNumbers(BaseModel):
    enclosed_in_parentheses: bool = FieldInfo(alias="enclosedInParentheses")

    operator: Literal["MULTIPLY_NUMBERS"]

    inputs: Optional[List[object]] = None

    property_name: Optional[str] = FieldInfo(alias="propertyName", default=None)

    value: Optional[float] = None


class CreatedObjectsPropertyRollupExpressionConditionalExpressionCmsMediabridgeDivideNumbers(BaseModel):
    enclosed_in_parentheses: bool = FieldInfo(alias="enclosedInParentheses")

    operator: Literal["DIVIDE_NUMBERS"]

    inputs: Optional[List[object]] = None

    property_name: Optional[str] = FieldInfo(alias="propertyName", default=None)

    value: Optional[float] = None


class CreatedObjectsPropertyRollupExpressionConditionalExpressionCmsMediabridgeRoundDownNumbers(BaseModel):
    operator: Literal["ROUND_DOWN"]

    inputs: Optional[List[object]] = None

    property_name: Optional[str] = FieldInfo(alias="propertyName", default=None)

    value: Optional[float] = None


class CreatedObjectsPropertyRollupExpressionConditionalExpressionCmsMediabridgeRoundUpNumbers(BaseModel):
    operator: Literal["ROUND_UP"]

    inputs: Optional[List[object]] = None

    property_name: Optional[str] = FieldInfo(alias="propertyName", default=None)

    value: Optional[float] = None


class CreatedObjectsPropertyRollupExpressionConditionalExpressionCmsMediabridgeRoundNearestNumbers(BaseModel):
    operator: Literal["ROUND_NEAREST"]

    inputs: Optional[List[object]] = None

    property_name: Optional[str] = FieldInfo(alias="propertyName", default=None)

    value: Optional[float] = None


class CreatedObjectsPropertyRollupExpressionConditionalExpressionCmsMediabridgeUpperCase(BaseModel):
    operator: Literal["UPPER_CASE"]

    inputs: Optional[List[object]] = None

    property_name: Optional[str] = FieldInfo(alias="propertyName", default=None)

    value: Optional[str] = None


class CreatedObjectsPropertyRollupExpressionConditionalExpressionCmsMediabridgeLowerCase(BaseModel):
    operator: Literal["LOWER_CASE"]

    inputs: Optional[List[object]] = None

    property_name: Optional[str] = FieldInfo(alias="propertyName", default=None)

    value: Optional[str] = None


class CreatedObjectsPropertyRollupExpressionConditionalExpressionCmsMediabridgeConcatStrings(BaseModel):
    operator: Literal["CONCAT_STRINGS"]

    inputs: Optional[List[object]] = None

    property_name: Optional[str] = FieldInfo(alias="propertyName", default=None)

    value: Optional[str] = None


class CreatedObjectsPropertyRollupExpressionConditionalExpressionCmsMediabridgeContains(BaseModel):
    operator: Literal["CONTAINS"]

    string_to_check: object = FieldInfo(alias="stringToCheck")

    inputs: Optional[List[object]] = None

    property_name: Optional[str] = FieldInfo(alias="propertyName", default=None)

    value: Optional[bool] = None


class CreatedObjectsPropertyRollupExpressionConditionalExpressionCmsMediabridgeBeginsWith(BaseModel):
    operator: Literal["BEGINS_WITH"]

    string_to_check: object = FieldInfo(alias="stringToCheck")

    inputs: Optional[List[object]] = None

    property_name: Optional[str] = FieldInfo(alias="propertyName", default=None)

    value: Optional[bool] = None


class CreatedObjectsPropertyRollupExpressionConditionalExpressionCmsMediabridgeNumberToString(BaseModel):
    operator: Literal["NUMBER_TO_STRING"]

    inputs: Optional[List[object]] = None

    property_name: Optional[str] = FieldInfo(alias="propertyName", default=None)

    value: Optional[str] = None


class CreatedObjectsPropertyRollupExpressionConditionalExpressionCmsMediabridgeParseNumber(BaseModel):
    operator: Literal["PARSE_NUMBER"]

    inputs: Optional[List[object]] = None

    property_name: Optional[str] = FieldInfo(alias="propertyName", default=None)

    value: Optional[float] = None


class CreatedObjectsPropertyRollupExpressionConditionalExpressionCmsMediabridgeFetchExchangeRate(BaseModel):
    operator: Literal["FETCH_EXCHANGE_RATE"]

    inputs: Optional[List[object]] = None

    property_name: Optional[str] = FieldInfo(alias="propertyName", default=None)

    value: Optional[float] = None


class CreatedObjectsPropertyRollupExpressionConditionalExpressionCmsMediabridgeFetchCurrencyDecimalPlaces(BaseModel):
    operator: Literal["FETCH_CURRENCY_DECIMAL_PLACES"]

    inputs: Optional[List[object]] = None

    property_name: Optional[str] = FieldInfo(alias="propertyName", default=None)

    value: Optional[float] = None


class CreatedObjectsPropertyRollupExpressionConditionalExpressionCmsMediabridgeFetchSingleCurrencyPortalCurrency(
    BaseModel
):
    operator: Literal["FETCH_SINGLE_CURRENCY_PORTAL_CURRENCY"]

    inputs: Optional[List[object]] = None

    property_name: Optional[str] = FieldInfo(alias="propertyName", default=None)

    value: Optional[str] = None


class CreatedObjectsPropertyRollupExpressionConditionalExpressionCmsMediabridgeDatedExchangeRate(BaseModel):
    operator: Literal["DATED_EXCHANGE_RATE"]

    inputs: Optional[List[object]] = None

    property_name: Optional[str] = FieldInfo(alias="propertyName", default=None)

    value: Optional[float] = None


class CreatedObjectsPropertyRollupExpressionConditionalExpressionCmsMediabridgePipelineProbability(BaseModel):
    operator: Literal["PIPELINE_PROBABILITY"]

    inputs: Optional[List[object]] = None

    property_name: Optional[str] = FieldInfo(alias="propertyName", default=None)

    value: Optional[float] = None


class CreatedObjectsPropertyRollupExpressionConditionalExpressionCmsMediabridgeMaxNumbers(BaseModel):
    operator: Literal["MAX_NUMBERS"]

    inputs: Optional[List[object]] = None

    property_name: Optional[str] = FieldInfo(alias="propertyName", default=None)

    value: Optional[float] = None


class CreatedObjectsPropertyRollupExpressionConditionalExpressionCmsMediabridgeMinNumbers(BaseModel):
    operator: Literal["MIN_NUMBERS"]

    inputs: Optional[List[object]] = None

    property_name: Optional[str] = FieldInfo(alias="propertyName", default=None)

    value: Optional[float] = None


class CreatedObjectsPropertyRollupExpressionConditionalExpressionCmsMediabridgeLessThan(BaseModel):
    operator: Literal["LESS_THAN"]

    inputs: Optional[List[object]] = None

    property_name: Optional[str] = FieldInfo(alias="propertyName", default=None)

    value: Optional[bool] = None


class CreatedObjectsPropertyRollupExpressionConditionalExpressionCmsMediabridgeLessThanOrEqual(BaseModel):
    operator: Literal["LESS_THAN_OR_EQUAL"]

    inputs: Optional[List[object]] = None

    property_name: Optional[str] = FieldInfo(alias="propertyName", default=None)

    value: Optional[bool] = None


class CreatedObjectsPropertyRollupExpressionConditionalExpressionCmsMediabridgeMoreThan(BaseModel):
    operator: Literal["MORE_THAN"]

    inputs: Optional[List[object]] = None

    property_name: Optional[str] = FieldInfo(alias="propertyName", default=None)

    value: Optional[bool] = None


class CreatedObjectsPropertyRollupExpressionConditionalExpressionCmsMediabridgeMoreThanOrEqual(BaseModel):
    operator: Literal["MORE_THAN_OR_EQUAL"]

    inputs: Optional[List[object]] = None

    property_name: Optional[str] = FieldInfo(alias="propertyName", default=None)

    value: Optional[bool] = None


class CreatedObjectsPropertyRollupExpressionConditionalExpressionCmsMediabridgeNumberEquals(BaseModel):
    operator: Literal["NUMBER_EQUALS"]

    inputs: Optional[List[object]] = None

    property_name: Optional[str] = FieldInfo(alias="propertyName", default=None)

    value: Optional[bool] = None


class CreatedObjectsPropertyRollupExpressionConditionalExpressionCmsMediabridgeStringEquals(BaseModel):
    operator: Literal["STRING_EQUALS"]

    inputs: Optional[List[object]] = None

    property_name: Optional[str] = FieldInfo(alias="propertyName", default=None)

    value: Optional[bool] = None


class CreatedObjectsPropertyRollupExpressionConditionalExpressionCmsMediabridgeIsPipelineStageClosed(BaseModel):
    operator: Literal["IS_PIPELINE_STAGE_CLOSED"]

    inputs: Optional[List[object]] = None

    property_name: Optional[str] = FieldInfo(alias="propertyName", default=None)

    value: Optional[bool] = None


class CreatedObjectsPropertyRollupExpressionConditionalExpressionCmsMediabridgeNot(BaseModel):
    operator: Literal["NOT"]

    inputs: Optional[List[object]] = None

    property_name: Optional[str] = FieldInfo(alias="propertyName", default=None)

    value: Optional[bool] = None


class CreatedObjectsPropertyRollupExpressionConditionalExpressionCmsMediabridgeDate(BaseModel):
    operator: Literal["DATE"]

    inputs: Optional[List[object]] = None

    property_name: Optional[str] = FieldInfo(alias="propertyName", default=None)

    value: Optional[float] = None


class CreatedObjectsPropertyRollupExpressionConditionalExpressionCmsMediabridgeMonth(BaseModel):
    operator: Literal["MONTH"]

    inputs: Optional[List[object]] = None

    property_name: Optional[str] = FieldInfo(alias="propertyName", default=None)

    value: Optional[float] = None


class CreatedObjectsPropertyRollupExpressionConditionalExpressionCmsMediabridgeYear(BaseModel):
    operator: Literal["YEAR"]

    inputs: Optional[List[object]] = None

    property_name: Optional[str] = FieldInfo(alias="propertyName", default=None)

    value: Optional[float] = None


class CreatedObjectsPropertyRollupExpressionConditionalExpressionCmsMediabridgeNow(BaseModel):
    operator: Literal["NOW"]

    inputs: Optional[List[object]] = None

    property_name: Optional[str] = FieldInfo(alias="propertyName", default=None)

    value: Optional[float] = None


class CreatedObjectsPropertyRollupExpressionConditionalExpressionCmsMediabridgeTimeBetween(BaseModel):
    operator: Literal["TIME_BETWEEN"]

    inputs: Optional[List[object]] = None

    property_name: Optional[str] = FieldInfo(alias="propertyName", default=None)

    value: Optional[float] = None


class CreatedObjectsPropertyRollupExpressionConditionalExpressionCmsMediabridgePeriodToMonths(BaseModel):
    operator: Literal["PERIOD_TO_MONTHS"]

    inputs: Optional[List[object]] = None

    property_name: Optional[str] = FieldInfo(alias="propertyName", default=None)

    value: Optional[float] = None


class CreatedObjectsPropertyRollupExpressionConditionalExpressionCmsMediabridgePeriodToWeeks(BaseModel):
    operator: Literal["PERIOD_TO_WEEKS"]

    inputs: Optional[List[object]] = None

    property_name: Optional[str] = FieldInfo(alias="propertyName", default=None)

    value: Optional[float] = None


class CreatedObjectsPropertyRollupExpressionConditionalExpressionCmsMediabridgeAnd(BaseModel):
    enclosed_in_parentheses: bool = FieldInfo(alias="enclosedInParentheses")

    operator: Literal["AND"]

    inputs: Optional[List[object]] = None

    property_name: Optional[str] = FieldInfo(alias="propertyName", default=None)

    value: Optional[bool] = None


class CreatedObjectsPropertyRollupExpressionConditionalExpressionCmsMediabridgeOr(BaseModel):
    enclosed_in_parentheses: bool = FieldInfo(alias="enclosedInParentheses")

    operator: Literal["OR"]

    inputs: Optional[List[object]] = None

    property_name: Optional[str] = FieldInfo(alias="propertyName", default=None)

    value: Optional[bool] = None


class CreatedObjectsPropertyRollupExpressionConditionalExpressionCmsMediabridgeXor(BaseModel):
    enclosed_in_parentheses: bool = FieldInfo(alias="enclosedInParentheses")

    operator: Literal["XOR"]

    inputs: Optional[List[object]] = None

    property_name: Optional[str] = FieldInfo(alias="propertyName", default=None)

    value: Optional[bool] = None


class CreatedObjectsPropertyRollupExpressionConditionalExpressionCmsMediabridgeIfString(BaseModel):
    enclosed_in_parentheses: bool = FieldInfo(alias="enclosedInParentheses")

    if_expression: object = FieldInfo(alias="ifExpression")

    operator: Literal["IF_STRING"]

    else_expression: Optional[object] = FieldInfo(alias="elseExpression", default=None)

    inputs: Optional[List[object]] = None

    property_name: Optional[str] = FieldInfo(alias="propertyName", default=None)

    value: Optional[str] = None


class CreatedObjectsPropertyRollupExpressionConditionalExpressionCmsMediabridgeIfNumber(BaseModel):
    enclosed_in_parentheses: bool = FieldInfo(alias="enclosedInParentheses")

    if_expression: object = FieldInfo(alias="ifExpression")

    operator: Literal["IF_NUMBER"]

    else_expression: Optional[object] = FieldInfo(alias="elseExpression", default=None)

    inputs: Optional[List[object]] = None

    property_name: Optional[str] = FieldInfo(alias="propertyName", default=None)

    value: Optional[float] = None


class CreatedObjectsPropertyRollupExpressionConditionalExpressionCmsMediabridgeIfBoolean(BaseModel):
    enclosed_in_parentheses: bool = FieldInfo(alias="enclosedInParentheses")

    if_expression: object = FieldInfo(alias="ifExpression")

    operator: Literal["IF_BOOLEAN"]

    else_expression: Optional[object] = FieldInfo(alias="elseExpression", default=None)

    inputs: Optional[List[object]] = None

    property_name: Optional[str] = FieldInfo(alias="propertyName", default=None)

    value: Optional[bool] = None


class CreatedObjectsPropertyRollupExpressionConditionalExpressionCmsMediabridgeIsPresent(BaseModel):
    expression_to_evaluate: object = FieldInfo(alias="expressionToEvaluate")

    operator: Literal["IS_PRESENT"]

    inputs: Optional[List[object]] = None

    property_name: Optional[str] = FieldInfo(alias="propertyName", default=None)

    value: Optional[bool] = None


class CreatedObjectsPropertyRollupExpressionConditionalExpressionCmsMediabridgeHasEmailReply(BaseModel):
    operator: Literal["HAS_EMAIL_REPLY"]

    inputs: Optional[List[object]] = None

    property_name: Optional[str] = FieldInfo(alias="propertyName", default=None)

    value: Optional[bool] = None


class CreatedObjectsPropertyRollupExpressionConditionalExpressionCmsMediabridgeHasPlainTextEmailReply(BaseModel):
    operator: Literal["HAS_PLAIN_TEXT_EMAIL_REPLY"]

    inputs: Optional[List[object]] = None

    property_name: Optional[str] = FieldInfo(alias="propertyName", default=None)

    value: Optional[bool] = None


class CreatedObjectsPropertyRollupExpressionConditionalExpressionCmsMediabridgeExtractMostRecentEmailReplyHTML(
    BaseModel
):
    operator: Literal["EXTRACT_MOST_RECENT_EMAIL_REPLY_HTML"]

    inputs: Optional[List[object]] = None

    property_name: Optional[str] = FieldInfo(alias="propertyName", default=None)

    value: Optional[str] = None


class CreatedObjectsPropertyRollupExpressionConditionalExpressionCmsMediabridgeExtractMostRecentEmailReplyText(
    BaseModel
):
    operator: Literal["EXTRACT_MOST_RECENT_EMAIL_REPLY_TEXT"]

    inputs: Optional[List[object]] = None

    property_name: Optional[str] = FieldInfo(alias="propertyName", default=None)

    value: Optional[str] = None


class CreatedObjectsPropertyRollupExpressionConditionalExpressionCmsMediabridgeExtractMostRecentPlainTextEmailReply(
    BaseModel
):
    operator: Literal["EXTRACT_MOST_RECENT_PLAIN_TEXT_EMAIL_REPLY"]

    inputs: Optional[List[object]] = None

    property_name: Optional[str] = FieldInfo(alias="propertyName", default=None)

    value: Optional[str] = None


class CreatedObjectsPropertyRollupExpressionConditionalExpressionCmsMediabridgeSetContainsString(BaseModel):
    operator: Literal["SET_CONTAINS_STRING"]

    string_to_check: object = FieldInfo(alias="stringToCheck")

    inputs: Optional[List[object]] = None

    property_name: Optional[str] = FieldInfo(alias="propertyName", default=None)

    value: Optional[bool] = None


class CreatedObjectsPropertyRollupExpressionConditionalExpressionCmsMediabridgeIsEngagementType(BaseModel):
    operator: Literal["IS_ENGAGEMENT_TYPE"]

    inputs: Optional[List[object]] = None

    property_name: Optional[str] = FieldInfo(alias="propertyName", default=None)

    value: Optional[bool] = None


class CreatedObjectsPropertyRollupExpressionConditionalExpressionCmsMediabridgeFormatFullName(BaseModel):
    operator: Literal["FORMAT_FULL_NAME"]

    inputs: Optional[List[object]] = None

    property_name: Optional[str] = FieldInfo(alias="propertyName", default=None)

    value: Optional[str] = None


class CreatedObjectsPropertyRollupExpressionConditionalExpressionCmsMediabridgeAbsoluteValue(BaseModel):
    operator: Literal["ABSOLUTE_VALUE"]

    inputs: Optional[List[object]] = None

    property_name: Optional[str] = FieldInfo(alias="propertyName", default=None)

    value: Optional[float] = None


class CreatedObjectsPropertyRollupExpressionConditionalExpressionCmsMediabridgeSquareRoot(BaseModel):
    operator: Literal["SQUARE_ROOT"]

    inputs: Optional[List[object]] = None

    property_name: Optional[str] = FieldInfo(alias="propertyName", default=None)

    value: Optional[float] = None


class CreatedObjectsPropertyRollupExpressionConditionalExpressionCmsMediabridgePower(BaseModel):
    operator: Literal["POWER"]

    inputs: Optional[List[object]] = None

    property_name: Optional[str] = FieldInfo(alias="propertyName", default=None)

    value: Optional[float] = None


class CreatedObjectsPropertyRollupExpressionConditionalExpressionCmsMediabridgeSubstring(BaseModel):
    operator: Literal["SUBSTRING"]

    string_to_check: object = FieldInfo(alias="stringToCheck")

    inputs: Optional[List[object]] = None

    property_name: Optional[str] = FieldInfo(alias="propertyName", default=None)

    value: Optional[str] = None


class CreatedObjectsPropertyRollupExpressionConditionalExpressionCmsMediabridgeEuler(BaseModel):
    operator: Literal["EULER"]

    inputs: Optional[List[object]] = None

    property_name: Optional[str] = FieldInfo(alias="propertyName", default=None)

    value: Optional[float] = None


class CreatedObjectsPropertyRollupExpressionConditionalExpressionCmsMediabridgeStringLength(BaseModel):
    operator: Literal["STRING_LENGTH"]

    inputs: Optional[List[object]] = None

    property_name: Optional[str] = FieldInfo(alias="propertyName", default=None)

    value: Optional[float] = None


class CreatedObjectsPropertyRollupExpressionConditionalExpressionCmsMediabridgeAddTime(BaseModel):
    operator: Literal["ADD_TIME"]

    string_to_check: object = FieldInfo(alias="stringToCheck")

    inputs: Optional[List[object]] = None

    property_name: Optional[str] = FieldInfo(alias="propertyName", default=None)

    value: Optional[float] = None


class CreatedObjectsPropertyRollupExpressionConditionalExpressionCmsMediabridgeSubtractTime(BaseModel):
    operator: Literal["SUBTRACT_TIME"]

    string_to_check: object = FieldInfo(alias="stringToCheck")

    inputs: Optional[List[object]] = None

    property_name: Optional[str] = FieldInfo(alias="propertyName", default=None)

    value: Optional[float] = None


CreatedObjectsPropertyRollupExpressionConditionalExpression: TypeAlias = Union[
    CreatedObjectsPropertyRollupExpressionConditionalExpressionCmsMediabridgeConstantBoolean,
    CreatedObjectsPropertyRollupExpressionConditionalExpressionCmsMediabridgeConstantNumber,
    CreatedObjectsPropertyRollupExpressionConditionalExpressionCmsMediabridgeConstantString,
    CreatedObjectsPropertyRollupExpressionConditionalExpressionCmsMediabridgeBooleanPropertyVariable,
    CreatedObjectsPropertyRollupExpressionConditionalExpressionCmsMediabridgeStringPropertyVariable,
    CreatedObjectsPropertyRollupExpressionConditionalExpressionCmsMediabridgeNumberPropertyVariable,
    CreatedObjectsPropertyRollupExpressionConditionalExpressionCmsMediabridgeTimestampOfPropertyVariable,
    CreatedObjectsPropertyRollupExpressionConditionalExpressionCmsMediabridgeBooleanTargetPropertyVariable,
    CreatedObjectsPropertyRollupExpressionConditionalExpressionCmsMediabridgeStringTargetPropertyVariable,
    CreatedObjectsPropertyRollupExpressionConditionalExpressionCmsMediabridgeNumberTargetPropertyVariable,
    CreatedObjectsPropertyRollupExpressionConditionalExpressionCmsMediabridgeTimestampOfTargetPropertyVariable,
    CreatedObjectsPropertyRollupExpressionConditionalExpressionCmsMediabridgeAddNumbers,
    CreatedObjectsPropertyRollupExpressionConditionalExpressionCmsMediabridgeSubtractNumbers,
    CreatedObjectsPropertyRollupExpressionConditionalExpressionCmsMediabridgeMultiplyNumbers,
    CreatedObjectsPropertyRollupExpressionConditionalExpressionCmsMediabridgeDivideNumbers,
    CreatedObjectsPropertyRollupExpressionConditionalExpressionCmsMediabridgeRoundDownNumbers,
    CreatedObjectsPropertyRollupExpressionConditionalExpressionCmsMediabridgeRoundUpNumbers,
    CreatedObjectsPropertyRollupExpressionConditionalExpressionCmsMediabridgeRoundNearestNumbers,
    CreatedObjectsPropertyRollupExpressionConditionalExpressionCmsMediabridgeUpperCase,
    CreatedObjectsPropertyRollupExpressionConditionalExpressionCmsMediabridgeLowerCase,
    CreatedObjectsPropertyRollupExpressionConditionalExpressionCmsMediabridgeConcatStrings,
    CreatedObjectsPropertyRollupExpressionConditionalExpressionCmsMediabridgeContains,
    CreatedObjectsPropertyRollupExpressionConditionalExpressionCmsMediabridgeBeginsWith,
    CreatedObjectsPropertyRollupExpressionConditionalExpressionCmsMediabridgeNumberToString,
    CreatedObjectsPropertyRollupExpressionConditionalExpressionCmsMediabridgeParseNumber,
    CreatedObjectsPropertyRollupExpressionConditionalExpressionCmsMediabridgeFetchExchangeRate,
    CreatedObjectsPropertyRollupExpressionConditionalExpressionCmsMediabridgeFetchCurrencyDecimalPlaces,
    CreatedObjectsPropertyRollupExpressionConditionalExpressionCmsMediabridgeFetchSingleCurrencyPortalCurrency,
    CreatedObjectsPropertyRollupExpressionConditionalExpressionCmsMediabridgeDatedExchangeRate,
    CreatedObjectsPropertyRollupExpressionConditionalExpressionCmsMediabridgePipelineProbability,
    CreatedObjectsPropertyRollupExpressionConditionalExpressionCmsMediabridgeMaxNumbers,
    CreatedObjectsPropertyRollupExpressionConditionalExpressionCmsMediabridgeMinNumbers,
    CreatedObjectsPropertyRollupExpressionConditionalExpressionCmsMediabridgeLessThan,
    CreatedObjectsPropertyRollupExpressionConditionalExpressionCmsMediabridgeLessThanOrEqual,
    CreatedObjectsPropertyRollupExpressionConditionalExpressionCmsMediabridgeMoreThan,
    CreatedObjectsPropertyRollupExpressionConditionalExpressionCmsMediabridgeMoreThanOrEqual,
    CreatedObjectsPropertyRollupExpressionConditionalExpressionCmsMediabridgeNumberEquals,
    CreatedObjectsPropertyRollupExpressionConditionalExpressionCmsMediabridgeStringEquals,
    CreatedObjectsPropertyRollupExpressionConditionalExpressionCmsMediabridgeIsPipelineStageClosed,
    CreatedObjectsPropertyRollupExpressionConditionalExpressionCmsMediabridgeNot,
    CreatedObjectsPropertyRollupExpressionConditionalExpressionCmsMediabridgeDate,
    CreatedObjectsPropertyRollupExpressionConditionalExpressionCmsMediabridgeMonth,
    CreatedObjectsPropertyRollupExpressionConditionalExpressionCmsMediabridgeYear,
    CreatedObjectsPropertyRollupExpressionConditionalExpressionCmsMediabridgeNow,
    CreatedObjectsPropertyRollupExpressionConditionalExpressionCmsMediabridgeTimeBetween,
    CreatedObjectsPropertyRollupExpressionConditionalExpressionCmsMediabridgePeriodToMonths,
    CreatedObjectsPropertyRollupExpressionConditionalExpressionCmsMediabridgePeriodToWeeks,
    CreatedObjectsPropertyRollupExpressionConditionalExpressionCmsMediabridgeAnd,
    CreatedObjectsPropertyRollupExpressionConditionalExpressionCmsMediabridgeOr,
    CreatedObjectsPropertyRollupExpressionConditionalExpressionCmsMediabridgeXor,
    CreatedObjectsPropertyRollupExpressionConditionalExpressionCmsMediabridgeIfString,
    CreatedObjectsPropertyRollupExpressionConditionalExpressionCmsMediabridgeIfNumber,
    CreatedObjectsPropertyRollupExpressionConditionalExpressionCmsMediabridgeIfBoolean,
    CreatedObjectsPropertyRollupExpressionConditionalExpressionCmsMediabridgeIsPresent,
    CreatedObjectsPropertyRollupExpressionConditionalExpressionCmsMediabridgeHasEmailReply,
    CreatedObjectsPropertyRollupExpressionConditionalExpressionCmsMediabridgeHasPlainTextEmailReply,
    CreatedObjectsPropertyRollupExpressionConditionalExpressionCmsMediabridgeExtractMostRecentEmailReplyHTML,
    CreatedObjectsPropertyRollupExpressionConditionalExpressionCmsMediabridgeExtractMostRecentEmailReplyText,
    CreatedObjectsPropertyRollupExpressionConditionalExpressionCmsMediabridgeExtractMostRecentPlainTextEmailReply,
    CreatedObjectsPropertyRollupExpressionConditionalExpressionCmsMediabridgeSetContainsString,
    CreatedObjectsPropertyRollupExpressionConditionalExpressionCmsMediabridgeIsEngagementType,
    CreatedObjectsPropertyRollupExpressionConditionalExpressionCmsMediabridgeFormatFullName,
    CreatedObjectsPropertyRollupExpressionConditionalExpressionCmsMediabridgeAbsoluteValue,
    CreatedObjectsPropertyRollupExpressionConditionalExpressionCmsMediabridgeSquareRoot,
    CreatedObjectsPropertyRollupExpressionConditionalExpressionCmsMediabridgePower,
    CreatedObjectsPropertyRollupExpressionConditionalExpressionCmsMediabridgeSubstring,
    CreatedObjectsPropertyRollupExpressionConditionalExpressionCmsMediabridgeEuler,
    CreatedObjectsPropertyRollupExpressionConditionalExpressionCmsMediabridgeStringLength,
    CreatedObjectsPropertyRollupExpressionConditionalExpressionCmsMediabridgeAddTime,
    CreatedObjectsPropertyRollupExpressionConditionalExpressionCmsMediabridgeSubtractTime,
]


class CreatedObjectsPropertyRollupExpression(BaseModel):
    association_types: List[AssociationSpec] = FieldInfo(alias="associationTypes")

    rollup_operator: str = FieldInfo(alias="rollupOperator")

    source_object_type_id: str = FieldInfo(alias="sourceObjectTypeId")

    source_property_name: str = FieldInfo(alias="sourcePropertyName")

    conditional_expression: Optional[CreatedObjectsPropertyRollupExpressionConditionalExpression] = FieldInfo(
        alias="conditionalExpression", default=None
    )

    conditional_formula: Optional[str] = FieldInfo(alias="conditionalFormula", default=None)

    empty_rollup_value: Optional[str] = FieldInfo(alias="emptyRollupValue", default=None)

    source_compare_by_property_name: Optional[str] = FieldInfo(alias="sourceCompareByPropertyName", default=None)


class CreatedObjectsProperty(BaseModel):
    object_type_id: str = FieldInfo(alias="objectTypeId")

    property: Property
    """Defines a property"""

    calculation_expression: Optional[CreatedObjectsPropertyCalculationExpression] = FieldInfo(
        alias="calculationExpression", default=None
    )

    calculation_formula: Optional[str] = FieldInfo(alias="calculationFormula", default=None)

    definition_source: Optional[CreatedObjectsPropertyDefinitionSource] = FieldInfo(
        alias="definitionSource", default=None
    )

    extension_data: Optional[CreatedObjectsPropertyExtensionData] = FieldInfo(alias="extensionData", default=None)

    external_options_meta_data: Optional[CreatedObjectsPropertyExternalOptionsMetaData] = FieldInfo(
        alias="externalOptionsMetaData", default=None
    )

    fulcrum_portal_id: Optional[int] = FieldInfo(alias="fulcrumPortalId", default=None)

    fulcrum_timestamp: Optional[int] = FieldInfo(alias="fulcrumTimestamp", default=None)

    janus_group: Optional[str] = FieldInfo(alias="janusGroup", default=None)

    permission: Optional[CreatedObjectsPropertyPermission] = None

    property_definition_source: Optional[CreatedObjectsPropertyPropertyDefinitionSource] = FieldInfo(
        alias="propertyDefinitionSource", default=None
    )

    property_requirements: Optional[CreatedObjectsPropertyPropertyRequirements] = FieldInfo(
        alias="propertyRequirements", default=None
    )

    rollup_expression: Optional[CreatedObjectsPropertyRollupExpression] = FieldInfo(
        alias="rollupExpression", default=None
    )


class CreatedObjectsPropertyGroup(BaseModel):
    deleted: bool

    display_name: str = FieldInfo(alias="displayName")

    display_order: int = FieldInfo(alias="displayOrder")

    fulcrum_portal_id: int = FieldInfo(alias="fulcrumPortalId")

    fulcrum_timestamp: int = FieldInfo(alias="fulcrumTimestamp")

    hubspot_defined: bool = FieldInfo(alias="hubspotDefined")

    name: str

    portal_id: int = FieldInfo(alias="portalId")


class CreatedObjects(BaseModel):
    object_type: CreatedObjectsObjectType = FieldInfo(alias="objectType")

    properties: List[CreatedObjectsProperty]

    property_groups: List[CreatedObjectsPropertyGroup] = FieldInfo(alias="propertyGroups")


class IntegratorSettingCreateObjectDefinitionResponse(BaseModel):
    created_objects: Dict[str, CreatedObjects] = FieldInfo(alias="createdObjects")
