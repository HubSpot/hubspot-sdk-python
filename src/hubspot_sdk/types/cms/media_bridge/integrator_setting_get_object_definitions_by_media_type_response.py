# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from ...shared import property as _property
from ...._models import BaseModel
from ...shared.association_spec import AssociationSpec

__all__ = [
    "IntegratorSettingGetObjectDefinitionsByMediaTypeResponse",
    "Property",
    "PropertyCalculationExpression",
    "PropertyCalculationExpressionCmsMediabridgeConstantBoolean",
    "PropertyCalculationExpressionCmsMediabridgeConstantNumber",
    "PropertyCalculationExpressionCmsMediabridgeConstantString",
    "PropertyCalculationExpressionCmsMediabridgeBooleanPropertyVariable",
    "PropertyCalculationExpressionCmsMediabridgeStringPropertyVariable",
    "PropertyCalculationExpressionCmsMediabridgeNumberPropertyVariable",
    "PropertyCalculationExpressionCmsMediabridgeTimestampOfPropertyVariable",
    "PropertyCalculationExpressionCmsMediabridgeBooleanTargetPropertyVariable",
    "PropertyCalculationExpressionCmsMediabridgeStringTargetPropertyVariable",
    "PropertyCalculationExpressionCmsMediabridgeNumberTargetPropertyVariable",
    "PropertyCalculationExpressionCmsMediabridgeTimestampOfTargetPropertyVariable",
    "PropertyCalculationExpressionCmsMediabridgeAddNumbers",
    "PropertyCalculationExpressionCmsMediabridgeSubtractNumbers",
    "PropertyCalculationExpressionCmsMediabridgeMultiplyNumbers",
    "PropertyCalculationExpressionCmsMediabridgeDivideNumbers",
    "PropertyCalculationExpressionCmsMediabridgeRoundDownNumbers",
    "PropertyCalculationExpressionCmsMediabridgeRoundUpNumbers",
    "PropertyCalculationExpressionCmsMediabridgeRoundNearestNumbers",
    "PropertyCalculationExpressionCmsMediabridgeUpperCase",
    "PropertyCalculationExpressionCmsMediabridgeLowerCase",
    "PropertyCalculationExpressionCmsMediabridgeConcatStrings",
    "PropertyCalculationExpressionCmsMediabridgeContains",
    "PropertyCalculationExpressionCmsMediabridgeBeginsWith",
    "PropertyCalculationExpressionCmsMediabridgeNumberToString",
    "PropertyCalculationExpressionCmsMediabridgeParseNumber",
    "PropertyCalculationExpressionCmsMediabridgeFetchExchangeRate",
    "PropertyCalculationExpressionCmsMediabridgeFetchCurrencyDecimalPlaces",
    "PropertyCalculationExpressionCmsMediabridgeFetchSingleCurrencyPortalCurrency",
    "PropertyCalculationExpressionCmsMediabridgeDatedExchangeRate",
    "PropertyCalculationExpressionCmsMediabridgePipelineProbability",
    "PropertyCalculationExpressionCmsMediabridgeMaxNumbers",
    "PropertyCalculationExpressionCmsMediabridgeMinNumbers",
    "PropertyCalculationExpressionCmsMediabridgeLessThan",
    "PropertyCalculationExpressionCmsMediabridgeLessThanOrEqual",
    "PropertyCalculationExpressionCmsMediabridgeMoreThan",
    "PropertyCalculationExpressionCmsMediabridgeMoreThanOrEqual",
    "PropertyCalculationExpressionCmsMediabridgeNumberEquals",
    "PropertyCalculationExpressionCmsMediabridgeStringEquals",
    "PropertyCalculationExpressionCmsMediabridgeIsPipelineStageClosed",
    "PropertyCalculationExpressionCmsMediabridgeNot",
    "PropertyCalculationExpressionCmsMediabridgeDate",
    "PropertyCalculationExpressionCmsMediabridgeMonth",
    "PropertyCalculationExpressionCmsMediabridgeYear",
    "PropertyCalculationExpressionCmsMediabridgeNow",
    "PropertyCalculationExpressionCmsMediabridgeTimeBetween",
    "PropertyCalculationExpressionCmsMediabridgePeriodToMonths",
    "PropertyCalculationExpressionCmsMediabridgePeriodToWeeks",
    "PropertyCalculationExpressionCmsMediabridgeAnd",
    "PropertyCalculationExpressionCmsMediabridgeOr",
    "PropertyCalculationExpressionCmsMediabridgeXor",
    "PropertyCalculationExpressionCmsMediabridgeIfString",
    "PropertyCalculationExpressionCmsMediabridgeIfNumber",
    "PropertyCalculationExpressionCmsMediabridgeIfBoolean",
    "PropertyCalculationExpressionCmsMediabridgeIsPresent",
    "PropertyCalculationExpressionCmsMediabridgeHasEmailReply",
    "PropertyCalculationExpressionCmsMediabridgeHasPlainTextEmailReply",
    "PropertyCalculationExpressionCmsMediabridgeExtractMostRecentEmailReplyHTML",
    "PropertyCalculationExpressionCmsMediabridgeExtractMostRecentEmailReplyText",
    "PropertyCalculationExpressionCmsMediabridgeExtractMostRecentPlainTextEmailReply",
    "PropertyCalculationExpressionCmsMediabridgeSetContainsString",
    "PropertyCalculationExpressionCmsMediabridgeIsEngagementType",
    "PropertyCalculationExpressionCmsMediabridgeFormatFullName",
    "PropertyCalculationExpressionCmsMediabridgeAbsoluteValue",
    "PropertyCalculationExpressionCmsMediabridgeSquareRoot",
    "PropertyCalculationExpressionCmsMediabridgePower",
    "PropertyCalculationExpressionCmsMediabridgeSubstring",
    "PropertyCalculationExpressionCmsMediabridgeEuler",
    "PropertyCalculationExpressionCmsMediabridgeStringLength",
    "PropertyCalculationExpressionCmsMediabridgeAddTime",
    "PropertyCalculationExpressionCmsMediabridgeSubtractTime",
    "PropertyDefinitionSource",
    "PropertyExtensionData",
    "PropertyExtensionDataCaseChangeTestExtensionData",
    "PropertyExtensionDataOptionDecoratorsExtensionData",
    "PropertyExtensionDataOptionDecoratorsExtensionDataOptionDecorators",
    "PropertyExtensionDataRequiredPropertiesExtensionData",
    "PropertyExtensionDataSoftRequiredPropertiesExtensionData",
    "PropertyExternalOptionsMetaData",
    "PropertyExternalOptionsMetaDataFilter",
    "PropertyPermission",
    "PropertyPropertyDefinitionSource",
    "PropertyPropertyRequirements",
    "PropertyRollupExpression",
    "PropertyRollupExpressionConditionalExpression",
    "PropertyRollupExpressionConditionalExpressionCmsMediabridgeConstantBoolean",
    "PropertyRollupExpressionConditionalExpressionCmsMediabridgeConstantNumber",
    "PropertyRollupExpressionConditionalExpressionCmsMediabridgeConstantString",
    "PropertyRollupExpressionConditionalExpressionCmsMediabridgeBooleanPropertyVariable",
    "PropertyRollupExpressionConditionalExpressionCmsMediabridgeStringPropertyVariable",
    "PropertyRollupExpressionConditionalExpressionCmsMediabridgeNumberPropertyVariable",
    "PropertyRollupExpressionConditionalExpressionCmsMediabridgeTimestampOfPropertyVariable",
    "PropertyRollupExpressionConditionalExpressionCmsMediabridgeBooleanTargetPropertyVariable",
    "PropertyRollupExpressionConditionalExpressionCmsMediabridgeStringTargetPropertyVariable",
    "PropertyRollupExpressionConditionalExpressionCmsMediabridgeNumberTargetPropertyVariable",
    "PropertyRollupExpressionConditionalExpressionCmsMediabridgeTimestampOfTargetPropertyVariable",
    "PropertyRollupExpressionConditionalExpressionCmsMediabridgeAddNumbers",
    "PropertyRollupExpressionConditionalExpressionCmsMediabridgeSubtractNumbers",
    "PropertyRollupExpressionConditionalExpressionCmsMediabridgeMultiplyNumbers",
    "PropertyRollupExpressionConditionalExpressionCmsMediabridgeDivideNumbers",
    "PropertyRollupExpressionConditionalExpressionCmsMediabridgeRoundDownNumbers",
    "PropertyRollupExpressionConditionalExpressionCmsMediabridgeRoundUpNumbers",
    "PropertyRollupExpressionConditionalExpressionCmsMediabridgeRoundNearestNumbers",
    "PropertyRollupExpressionConditionalExpressionCmsMediabridgeUpperCase",
    "PropertyRollupExpressionConditionalExpressionCmsMediabridgeLowerCase",
    "PropertyRollupExpressionConditionalExpressionCmsMediabridgeConcatStrings",
    "PropertyRollupExpressionConditionalExpressionCmsMediabridgeContains",
    "PropertyRollupExpressionConditionalExpressionCmsMediabridgeBeginsWith",
    "PropertyRollupExpressionConditionalExpressionCmsMediabridgeNumberToString",
    "PropertyRollupExpressionConditionalExpressionCmsMediabridgeParseNumber",
    "PropertyRollupExpressionConditionalExpressionCmsMediabridgeFetchExchangeRate",
    "PropertyRollupExpressionConditionalExpressionCmsMediabridgeFetchCurrencyDecimalPlaces",
    "PropertyRollupExpressionConditionalExpressionCmsMediabridgeFetchSingleCurrencyPortalCurrency",
    "PropertyRollupExpressionConditionalExpressionCmsMediabridgeDatedExchangeRate",
    "PropertyRollupExpressionConditionalExpressionCmsMediabridgePipelineProbability",
    "PropertyRollupExpressionConditionalExpressionCmsMediabridgeMaxNumbers",
    "PropertyRollupExpressionConditionalExpressionCmsMediabridgeMinNumbers",
    "PropertyRollupExpressionConditionalExpressionCmsMediabridgeLessThan",
    "PropertyRollupExpressionConditionalExpressionCmsMediabridgeLessThanOrEqual",
    "PropertyRollupExpressionConditionalExpressionCmsMediabridgeMoreThan",
    "PropertyRollupExpressionConditionalExpressionCmsMediabridgeMoreThanOrEqual",
    "PropertyRollupExpressionConditionalExpressionCmsMediabridgeNumberEquals",
    "PropertyRollupExpressionConditionalExpressionCmsMediabridgeStringEquals",
    "PropertyRollupExpressionConditionalExpressionCmsMediabridgeIsPipelineStageClosed",
    "PropertyRollupExpressionConditionalExpressionCmsMediabridgeNot",
    "PropertyRollupExpressionConditionalExpressionCmsMediabridgeDate",
    "PropertyRollupExpressionConditionalExpressionCmsMediabridgeMonth",
    "PropertyRollupExpressionConditionalExpressionCmsMediabridgeYear",
    "PropertyRollupExpressionConditionalExpressionCmsMediabridgeNow",
    "PropertyRollupExpressionConditionalExpressionCmsMediabridgeTimeBetween",
    "PropertyRollupExpressionConditionalExpressionCmsMediabridgePeriodToMonths",
    "PropertyRollupExpressionConditionalExpressionCmsMediabridgePeriodToWeeks",
    "PropertyRollupExpressionConditionalExpressionCmsMediabridgeAnd",
    "PropertyRollupExpressionConditionalExpressionCmsMediabridgeOr",
    "PropertyRollupExpressionConditionalExpressionCmsMediabridgeXor",
    "PropertyRollupExpressionConditionalExpressionCmsMediabridgeIfString",
    "PropertyRollupExpressionConditionalExpressionCmsMediabridgeIfNumber",
    "PropertyRollupExpressionConditionalExpressionCmsMediabridgeIfBoolean",
    "PropertyRollupExpressionConditionalExpressionCmsMediabridgeIsPresent",
    "PropertyRollupExpressionConditionalExpressionCmsMediabridgeHasEmailReply",
    "PropertyRollupExpressionConditionalExpressionCmsMediabridgeHasPlainTextEmailReply",
    "PropertyRollupExpressionConditionalExpressionCmsMediabridgeExtractMostRecentEmailReplyHTML",
    "PropertyRollupExpressionConditionalExpressionCmsMediabridgeExtractMostRecentEmailReplyText",
    "PropertyRollupExpressionConditionalExpressionCmsMediabridgeExtractMostRecentPlainTextEmailReply",
    "PropertyRollupExpressionConditionalExpressionCmsMediabridgeSetContainsString",
    "PropertyRollupExpressionConditionalExpressionCmsMediabridgeIsEngagementType",
    "PropertyRollupExpressionConditionalExpressionCmsMediabridgeFormatFullName",
    "PropertyRollupExpressionConditionalExpressionCmsMediabridgeAbsoluteValue",
    "PropertyRollupExpressionConditionalExpressionCmsMediabridgeSquareRoot",
    "PropertyRollupExpressionConditionalExpressionCmsMediabridgePower",
    "PropertyRollupExpressionConditionalExpressionCmsMediabridgeSubstring",
    "PropertyRollupExpressionConditionalExpressionCmsMediabridgeEuler",
    "PropertyRollupExpressionConditionalExpressionCmsMediabridgeStringLength",
    "PropertyRollupExpressionConditionalExpressionCmsMediabridgeAddTime",
    "PropertyRollupExpressionConditionalExpressionCmsMediabridgeSubtractTime",
    "PropertyGroup",
    "Schema",
    "SchemaScopeMapping",
]


class PropertyCalculationExpressionCmsMediabridgeConstantBoolean(BaseModel):
    operator: Literal["CONSTANT_BOOLEAN"]

    inputs: Optional[List[object]] = None

    property_name: Optional[str] = FieldInfo(alias="propertyName", default=None)

    value: Optional[bool] = None


class PropertyCalculationExpressionCmsMediabridgeConstantNumber(BaseModel):
    operator: Literal["CONSTANT_NUMBER"]

    inputs: Optional[List[object]] = None

    property_name: Optional[str] = FieldInfo(alias="propertyName", default=None)

    value: Optional[float] = None


class PropertyCalculationExpressionCmsMediabridgeConstantString(BaseModel):
    operator: Literal["CONSTANT_STRING"]

    inputs: Optional[List[object]] = None

    property_name: Optional[str] = FieldInfo(alias="propertyName", default=None)

    value: Optional[str] = None


class PropertyCalculationExpressionCmsMediabridgeBooleanPropertyVariable(BaseModel):
    operator: Literal["BOOLEAN_PROPERTY_VARIABLE"]

    inputs: Optional[List[object]] = None

    property_name: Optional[str] = FieldInfo(alias="propertyName", default=None)

    value: Optional[bool] = None


class PropertyCalculationExpressionCmsMediabridgeStringPropertyVariable(BaseModel):
    operator: Literal["STRING_PROPERTY_VARIABLE"]

    inputs: Optional[List[object]] = None

    property_name: Optional[str] = FieldInfo(alias="propertyName", default=None)

    value: Optional[str] = None


class PropertyCalculationExpressionCmsMediabridgeNumberPropertyVariable(BaseModel):
    operator: Literal["NUMBER_PROPERTY_VARIABLE"]

    inputs: Optional[List[object]] = None

    property_name: Optional[str] = FieldInfo(alias="propertyName", default=None)

    value: Optional[float] = None


class PropertyCalculationExpressionCmsMediabridgeTimestampOfPropertyVariable(BaseModel):
    operator: Literal["TIMESTAMP_OF_PROPERTY_VARIABLE"]

    inputs: Optional[List[object]] = None

    property_name: Optional[str] = FieldInfo(alias="propertyName", default=None)

    value: Optional[str] = None


class PropertyCalculationExpressionCmsMediabridgeBooleanTargetPropertyVariable(BaseModel):
    operator: Literal["BOOLEAN_TARGET_PROPERTY_VARIABLE"]

    inputs: Optional[List[object]] = None

    property_name: Optional[str] = FieldInfo(alias="propertyName", default=None)

    value: Optional[bool] = None


class PropertyCalculationExpressionCmsMediabridgeStringTargetPropertyVariable(BaseModel):
    operator: Literal["STRING_TARGET_PROPERTY_VARIABLE"]

    inputs: Optional[List[object]] = None

    property_name: Optional[str] = FieldInfo(alias="propertyName", default=None)

    value: Optional[str] = None


class PropertyCalculationExpressionCmsMediabridgeNumberTargetPropertyVariable(BaseModel):
    operator: Literal["NUMBER_TARGET_PROPERTY_VARIABLE"]

    inputs: Optional[List[object]] = None

    property_name: Optional[str] = FieldInfo(alias="propertyName", default=None)

    value: Optional[float] = None


class PropertyCalculationExpressionCmsMediabridgeTimestampOfTargetPropertyVariable(BaseModel):
    operator: Literal["TIMESTAMP_OF_TARGET_PROPERTY_VARIABLE"]

    inputs: Optional[List[object]] = None

    property_name: Optional[str] = FieldInfo(alias="propertyName", default=None)

    value: Optional[str] = None


class PropertyCalculationExpressionCmsMediabridgeAddNumbers(BaseModel):
    enclosed_in_parentheses: bool = FieldInfo(alias="enclosedInParentheses")

    operator: Literal["ADD_NUMBERS"]

    inputs: Optional[List[object]] = None

    property_name: Optional[str] = FieldInfo(alias="propertyName", default=None)

    value: Optional[float] = None


class PropertyCalculationExpressionCmsMediabridgeSubtractNumbers(BaseModel):
    enclosed_in_parentheses: bool = FieldInfo(alias="enclosedInParentheses")

    operator: Literal["SUBTRACT_NUMBERS"]

    inputs: Optional[List[object]] = None

    property_name: Optional[str] = FieldInfo(alias="propertyName", default=None)

    value: Optional[float] = None


class PropertyCalculationExpressionCmsMediabridgeMultiplyNumbers(BaseModel):
    enclosed_in_parentheses: bool = FieldInfo(alias="enclosedInParentheses")

    operator: Literal["MULTIPLY_NUMBERS"]

    inputs: Optional[List[object]] = None

    property_name: Optional[str] = FieldInfo(alias="propertyName", default=None)

    value: Optional[float] = None


class PropertyCalculationExpressionCmsMediabridgeDivideNumbers(BaseModel):
    enclosed_in_parentheses: bool = FieldInfo(alias="enclosedInParentheses")

    operator: Literal["DIVIDE_NUMBERS"]

    inputs: Optional[List[object]] = None

    property_name: Optional[str] = FieldInfo(alias="propertyName", default=None)

    value: Optional[float] = None


class PropertyCalculationExpressionCmsMediabridgeRoundDownNumbers(BaseModel):
    operator: Literal["ROUND_DOWN"]

    inputs: Optional[List[object]] = None

    property_name: Optional[str] = FieldInfo(alias="propertyName", default=None)

    value: Optional[float] = None


class PropertyCalculationExpressionCmsMediabridgeRoundUpNumbers(BaseModel):
    operator: Literal["ROUND_UP"]

    inputs: Optional[List[object]] = None

    property_name: Optional[str] = FieldInfo(alias="propertyName", default=None)

    value: Optional[float] = None


class PropertyCalculationExpressionCmsMediabridgeRoundNearestNumbers(BaseModel):
    operator: Literal["ROUND_NEAREST"]

    inputs: Optional[List[object]] = None

    property_name: Optional[str] = FieldInfo(alias="propertyName", default=None)

    value: Optional[float] = None


class PropertyCalculationExpressionCmsMediabridgeUpperCase(BaseModel):
    operator: Literal["UPPER_CASE"]

    inputs: Optional[List[object]] = None

    property_name: Optional[str] = FieldInfo(alias="propertyName", default=None)

    value: Optional[str] = None


class PropertyCalculationExpressionCmsMediabridgeLowerCase(BaseModel):
    operator: Literal["LOWER_CASE"]

    inputs: Optional[List[object]] = None

    property_name: Optional[str] = FieldInfo(alias="propertyName", default=None)

    value: Optional[str] = None


class PropertyCalculationExpressionCmsMediabridgeConcatStrings(BaseModel):
    operator: Literal["CONCAT_STRINGS"]

    inputs: Optional[List[object]] = None

    property_name: Optional[str] = FieldInfo(alias="propertyName", default=None)

    value: Optional[str] = None


class PropertyCalculationExpressionCmsMediabridgeContains(BaseModel):
    operator: Literal["CONTAINS"]

    string_to_check: object = FieldInfo(alias="stringToCheck")

    inputs: Optional[List[object]] = None

    property_name: Optional[str] = FieldInfo(alias="propertyName", default=None)

    value: Optional[bool] = None


class PropertyCalculationExpressionCmsMediabridgeBeginsWith(BaseModel):
    operator: Literal["BEGINS_WITH"]

    string_to_check: object = FieldInfo(alias="stringToCheck")

    inputs: Optional[List[object]] = None

    property_name: Optional[str] = FieldInfo(alias="propertyName", default=None)

    value: Optional[bool] = None


class PropertyCalculationExpressionCmsMediabridgeNumberToString(BaseModel):
    operator: Literal["NUMBER_TO_STRING"]

    inputs: Optional[List[object]] = None

    property_name: Optional[str] = FieldInfo(alias="propertyName", default=None)

    value: Optional[str] = None


class PropertyCalculationExpressionCmsMediabridgeParseNumber(BaseModel):
    operator: Literal["PARSE_NUMBER"]

    inputs: Optional[List[object]] = None

    property_name: Optional[str] = FieldInfo(alias="propertyName", default=None)

    value: Optional[float] = None


class PropertyCalculationExpressionCmsMediabridgeFetchExchangeRate(BaseModel):
    operator: Literal["FETCH_EXCHANGE_RATE"]

    inputs: Optional[List[object]] = None

    property_name: Optional[str] = FieldInfo(alias="propertyName", default=None)

    value: Optional[float] = None


class PropertyCalculationExpressionCmsMediabridgeFetchCurrencyDecimalPlaces(BaseModel):
    operator: Literal["FETCH_CURRENCY_DECIMAL_PLACES"]

    inputs: Optional[List[object]] = None

    property_name: Optional[str] = FieldInfo(alias="propertyName", default=None)

    value: Optional[float] = None


class PropertyCalculationExpressionCmsMediabridgeFetchSingleCurrencyPortalCurrency(BaseModel):
    operator: Literal["FETCH_SINGLE_CURRENCY_PORTAL_CURRENCY"]

    inputs: Optional[List[object]] = None

    property_name: Optional[str] = FieldInfo(alias="propertyName", default=None)

    value: Optional[str] = None


class PropertyCalculationExpressionCmsMediabridgeDatedExchangeRate(BaseModel):
    operator: Literal["DATED_EXCHANGE_RATE"]

    inputs: Optional[List[object]] = None

    property_name: Optional[str] = FieldInfo(alias="propertyName", default=None)

    value: Optional[float] = None


class PropertyCalculationExpressionCmsMediabridgePipelineProbability(BaseModel):
    operator: Literal["PIPELINE_PROBABILITY"]

    inputs: Optional[List[object]] = None

    property_name: Optional[str] = FieldInfo(alias="propertyName", default=None)

    value: Optional[float] = None


class PropertyCalculationExpressionCmsMediabridgeMaxNumbers(BaseModel):
    operator: Literal["MAX_NUMBERS"]

    inputs: Optional[List[object]] = None

    property_name: Optional[str] = FieldInfo(alias="propertyName", default=None)

    value: Optional[float] = None


class PropertyCalculationExpressionCmsMediabridgeMinNumbers(BaseModel):
    operator: Literal["MIN_NUMBERS"]

    inputs: Optional[List[object]] = None

    property_name: Optional[str] = FieldInfo(alias="propertyName", default=None)

    value: Optional[float] = None


class PropertyCalculationExpressionCmsMediabridgeLessThan(BaseModel):
    operator: Literal["LESS_THAN"]

    inputs: Optional[List[object]] = None

    property_name: Optional[str] = FieldInfo(alias="propertyName", default=None)

    value: Optional[bool] = None


class PropertyCalculationExpressionCmsMediabridgeLessThanOrEqual(BaseModel):
    operator: Literal["LESS_THAN_OR_EQUAL"]

    inputs: Optional[List[object]] = None

    property_name: Optional[str] = FieldInfo(alias="propertyName", default=None)

    value: Optional[bool] = None


class PropertyCalculationExpressionCmsMediabridgeMoreThan(BaseModel):
    operator: Literal["MORE_THAN"]

    inputs: Optional[List[object]] = None

    property_name: Optional[str] = FieldInfo(alias="propertyName", default=None)

    value: Optional[bool] = None


class PropertyCalculationExpressionCmsMediabridgeMoreThanOrEqual(BaseModel):
    operator: Literal["MORE_THAN_OR_EQUAL"]

    inputs: Optional[List[object]] = None

    property_name: Optional[str] = FieldInfo(alias="propertyName", default=None)

    value: Optional[bool] = None


class PropertyCalculationExpressionCmsMediabridgeNumberEquals(BaseModel):
    operator: Literal["NUMBER_EQUALS"]

    inputs: Optional[List[object]] = None

    property_name: Optional[str] = FieldInfo(alias="propertyName", default=None)

    value: Optional[bool] = None


class PropertyCalculationExpressionCmsMediabridgeStringEquals(BaseModel):
    operator: Literal["STRING_EQUALS"]

    inputs: Optional[List[object]] = None

    property_name: Optional[str] = FieldInfo(alias="propertyName", default=None)

    value: Optional[bool] = None


class PropertyCalculationExpressionCmsMediabridgeIsPipelineStageClosed(BaseModel):
    operator: Literal["IS_PIPELINE_STAGE_CLOSED"]

    inputs: Optional[List[object]] = None

    property_name: Optional[str] = FieldInfo(alias="propertyName", default=None)

    value: Optional[bool] = None


class PropertyCalculationExpressionCmsMediabridgeNot(BaseModel):
    operator: Literal["NOT"]

    inputs: Optional[List[object]] = None

    property_name: Optional[str] = FieldInfo(alias="propertyName", default=None)

    value: Optional[bool] = None


class PropertyCalculationExpressionCmsMediabridgeDate(BaseModel):
    operator: Literal["DATE"]

    inputs: Optional[List[object]] = None

    property_name: Optional[str] = FieldInfo(alias="propertyName", default=None)

    value: Optional[float] = None


class PropertyCalculationExpressionCmsMediabridgeMonth(BaseModel):
    operator: Literal["MONTH"]

    inputs: Optional[List[object]] = None

    property_name: Optional[str] = FieldInfo(alias="propertyName", default=None)

    value: Optional[float] = None


class PropertyCalculationExpressionCmsMediabridgeYear(BaseModel):
    operator: Literal["YEAR"]

    inputs: Optional[List[object]] = None

    property_name: Optional[str] = FieldInfo(alias="propertyName", default=None)

    value: Optional[float] = None


class PropertyCalculationExpressionCmsMediabridgeNow(BaseModel):
    operator: Literal["NOW"]

    inputs: Optional[List[object]] = None

    property_name: Optional[str] = FieldInfo(alias="propertyName", default=None)

    value: Optional[float] = None


class PropertyCalculationExpressionCmsMediabridgeTimeBetween(BaseModel):
    operator: Literal["TIME_BETWEEN"]

    inputs: Optional[List[object]] = None

    property_name: Optional[str] = FieldInfo(alias="propertyName", default=None)

    value: Optional[float] = None


class PropertyCalculationExpressionCmsMediabridgePeriodToMonths(BaseModel):
    operator: Literal["PERIOD_TO_MONTHS"]

    inputs: Optional[List[object]] = None

    property_name: Optional[str] = FieldInfo(alias="propertyName", default=None)

    value: Optional[float] = None


class PropertyCalculationExpressionCmsMediabridgePeriodToWeeks(BaseModel):
    operator: Literal["PERIOD_TO_WEEKS"]

    inputs: Optional[List[object]] = None

    property_name: Optional[str] = FieldInfo(alias="propertyName", default=None)

    value: Optional[float] = None


class PropertyCalculationExpressionCmsMediabridgeAnd(BaseModel):
    enclosed_in_parentheses: bool = FieldInfo(alias="enclosedInParentheses")

    operator: Literal["AND"]

    inputs: Optional[List[object]] = None

    property_name: Optional[str] = FieldInfo(alias="propertyName", default=None)

    value: Optional[bool] = None


class PropertyCalculationExpressionCmsMediabridgeOr(BaseModel):
    enclosed_in_parentheses: bool = FieldInfo(alias="enclosedInParentheses")

    operator: Literal["OR"]

    inputs: Optional[List[object]] = None

    property_name: Optional[str] = FieldInfo(alias="propertyName", default=None)

    value: Optional[bool] = None


class PropertyCalculationExpressionCmsMediabridgeXor(BaseModel):
    enclosed_in_parentheses: bool = FieldInfo(alias="enclosedInParentheses")

    operator: Literal["XOR"]

    inputs: Optional[List[object]] = None

    property_name: Optional[str] = FieldInfo(alias="propertyName", default=None)

    value: Optional[bool] = None


class PropertyCalculationExpressionCmsMediabridgeIfString(BaseModel):
    enclosed_in_parentheses: bool = FieldInfo(alias="enclosedInParentheses")

    if_expression: object = FieldInfo(alias="ifExpression")

    operator: Literal["IF_STRING"]

    else_expression: Optional[object] = FieldInfo(alias="elseExpression", default=None)

    inputs: Optional[List[object]] = None

    property_name: Optional[str] = FieldInfo(alias="propertyName", default=None)

    value: Optional[str] = None


class PropertyCalculationExpressionCmsMediabridgeIfNumber(BaseModel):
    enclosed_in_parentheses: bool = FieldInfo(alias="enclosedInParentheses")

    if_expression: object = FieldInfo(alias="ifExpression")

    operator: Literal["IF_NUMBER"]

    else_expression: Optional[object] = FieldInfo(alias="elseExpression", default=None)

    inputs: Optional[List[object]] = None

    property_name: Optional[str] = FieldInfo(alias="propertyName", default=None)

    value: Optional[float] = None


class PropertyCalculationExpressionCmsMediabridgeIfBoolean(BaseModel):
    enclosed_in_parentheses: bool = FieldInfo(alias="enclosedInParentheses")

    if_expression: object = FieldInfo(alias="ifExpression")

    operator: Literal["IF_BOOLEAN"]

    else_expression: Optional[object] = FieldInfo(alias="elseExpression", default=None)

    inputs: Optional[List[object]] = None

    property_name: Optional[str] = FieldInfo(alias="propertyName", default=None)

    value: Optional[bool] = None


class PropertyCalculationExpressionCmsMediabridgeIsPresent(BaseModel):
    expression_to_evaluate: object = FieldInfo(alias="expressionToEvaluate")

    operator: Literal["IS_PRESENT"]

    inputs: Optional[List[object]] = None

    property_name: Optional[str] = FieldInfo(alias="propertyName", default=None)

    value: Optional[bool] = None


class PropertyCalculationExpressionCmsMediabridgeHasEmailReply(BaseModel):
    operator: Literal["HAS_EMAIL_REPLY"]

    inputs: Optional[List[object]] = None

    property_name: Optional[str] = FieldInfo(alias="propertyName", default=None)

    value: Optional[bool] = None


class PropertyCalculationExpressionCmsMediabridgeHasPlainTextEmailReply(BaseModel):
    operator: Literal["HAS_PLAIN_TEXT_EMAIL_REPLY"]

    inputs: Optional[List[object]] = None

    property_name: Optional[str] = FieldInfo(alias="propertyName", default=None)

    value: Optional[bool] = None


class PropertyCalculationExpressionCmsMediabridgeExtractMostRecentEmailReplyHTML(BaseModel):
    operator: Literal["EXTRACT_MOST_RECENT_EMAIL_REPLY_HTML"]

    inputs: Optional[List[object]] = None

    property_name: Optional[str] = FieldInfo(alias="propertyName", default=None)

    value: Optional[str] = None


class PropertyCalculationExpressionCmsMediabridgeExtractMostRecentEmailReplyText(BaseModel):
    operator: Literal["EXTRACT_MOST_RECENT_EMAIL_REPLY_TEXT"]

    inputs: Optional[List[object]] = None

    property_name: Optional[str] = FieldInfo(alias="propertyName", default=None)

    value: Optional[str] = None


class PropertyCalculationExpressionCmsMediabridgeExtractMostRecentPlainTextEmailReply(BaseModel):
    operator: Literal["EXTRACT_MOST_RECENT_PLAIN_TEXT_EMAIL_REPLY"]

    inputs: Optional[List[object]] = None

    property_name: Optional[str] = FieldInfo(alias="propertyName", default=None)

    value: Optional[str] = None


class PropertyCalculationExpressionCmsMediabridgeSetContainsString(BaseModel):
    operator: Literal["SET_CONTAINS_STRING"]

    string_to_check: object = FieldInfo(alias="stringToCheck")

    inputs: Optional[List[object]] = None

    property_name: Optional[str] = FieldInfo(alias="propertyName", default=None)

    value: Optional[bool] = None


class PropertyCalculationExpressionCmsMediabridgeIsEngagementType(BaseModel):
    operator: Literal["IS_ENGAGEMENT_TYPE"]

    inputs: Optional[List[object]] = None

    property_name: Optional[str] = FieldInfo(alias="propertyName", default=None)

    value: Optional[bool] = None


class PropertyCalculationExpressionCmsMediabridgeFormatFullName(BaseModel):
    operator: Literal["FORMAT_FULL_NAME"]

    inputs: Optional[List[object]] = None

    property_name: Optional[str] = FieldInfo(alias="propertyName", default=None)

    value: Optional[str] = None


class PropertyCalculationExpressionCmsMediabridgeAbsoluteValue(BaseModel):
    operator: Literal["ABSOLUTE_VALUE"]

    inputs: Optional[List[object]] = None

    property_name: Optional[str] = FieldInfo(alias="propertyName", default=None)

    value: Optional[float] = None


class PropertyCalculationExpressionCmsMediabridgeSquareRoot(BaseModel):
    operator: Literal["SQUARE_ROOT"]

    inputs: Optional[List[object]] = None

    property_name: Optional[str] = FieldInfo(alias="propertyName", default=None)

    value: Optional[float] = None


class PropertyCalculationExpressionCmsMediabridgePower(BaseModel):
    operator: Literal["POWER"]

    inputs: Optional[List[object]] = None

    property_name: Optional[str] = FieldInfo(alias="propertyName", default=None)

    value: Optional[float] = None


class PropertyCalculationExpressionCmsMediabridgeSubstring(BaseModel):
    operator: Literal["SUBSTRING"]

    string_to_check: object = FieldInfo(alias="stringToCheck")

    inputs: Optional[List[object]] = None

    property_name: Optional[str] = FieldInfo(alias="propertyName", default=None)

    value: Optional[str] = None


class PropertyCalculationExpressionCmsMediabridgeEuler(BaseModel):
    operator: Literal["EULER"]

    inputs: Optional[List[object]] = None

    property_name: Optional[str] = FieldInfo(alias="propertyName", default=None)

    value: Optional[float] = None


class PropertyCalculationExpressionCmsMediabridgeStringLength(BaseModel):
    operator: Literal["STRING_LENGTH"]

    inputs: Optional[List[object]] = None

    property_name: Optional[str] = FieldInfo(alias="propertyName", default=None)

    value: Optional[float] = None


class PropertyCalculationExpressionCmsMediabridgeAddTime(BaseModel):
    operator: Literal["ADD_TIME"]

    string_to_check: object = FieldInfo(alias="stringToCheck")

    inputs: Optional[List[object]] = None

    property_name: Optional[str] = FieldInfo(alias="propertyName", default=None)

    value: Optional[float] = None


class PropertyCalculationExpressionCmsMediabridgeSubtractTime(BaseModel):
    operator: Literal["SUBTRACT_TIME"]

    string_to_check: object = FieldInfo(alias="stringToCheck")

    inputs: Optional[List[object]] = None

    property_name: Optional[str] = FieldInfo(alias="propertyName", default=None)

    value: Optional[float] = None


PropertyCalculationExpression: TypeAlias = Union[
    PropertyCalculationExpressionCmsMediabridgeConstantBoolean,
    PropertyCalculationExpressionCmsMediabridgeConstantNumber,
    PropertyCalculationExpressionCmsMediabridgeConstantString,
    PropertyCalculationExpressionCmsMediabridgeBooleanPropertyVariable,
    PropertyCalculationExpressionCmsMediabridgeStringPropertyVariable,
    PropertyCalculationExpressionCmsMediabridgeNumberPropertyVariable,
    PropertyCalculationExpressionCmsMediabridgeTimestampOfPropertyVariable,
    PropertyCalculationExpressionCmsMediabridgeBooleanTargetPropertyVariable,
    PropertyCalculationExpressionCmsMediabridgeStringTargetPropertyVariable,
    PropertyCalculationExpressionCmsMediabridgeNumberTargetPropertyVariable,
    PropertyCalculationExpressionCmsMediabridgeTimestampOfTargetPropertyVariable,
    PropertyCalculationExpressionCmsMediabridgeAddNumbers,
    PropertyCalculationExpressionCmsMediabridgeSubtractNumbers,
    PropertyCalculationExpressionCmsMediabridgeMultiplyNumbers,
    PropertyCalculationExpressionCmsMediabridgeDivideNumbers,
    PropertyCalculationExpressionCmsMediabridgeRoundDownNumbers,
    PropertyCalculationExpressionCmsMediabridgeRoundUpNumbers,
    PropertyCalculationExpressionCmsMediabridgeRoundNearestNumbers,
    PropertyCalculationExpressionCmsMediabridgeUpperCase,
    PropertyCalculationExpressionCmsMediabridgeLowerCase,
    PropertyCalculationExpressionCmsMediabridgeConcatStrings,
    PropertyCalculationExpressionCmsMediabridgeContains,
    PropertyCalculationExpressionCmsMediabridgeBeginsWith,
    PropertyCalculationExpressionCmsMediabridgeNumberToString,
    PropertyCalculationExpressionCmsMediabridgeParseNumber,
    PropertyCalculationExpressionCmsMediabridgeFetchExchangeRate,
    PropertyCalculationExpressionCmsMediabridgeFetchCurrencyDecimalPlaces,
    PropertyCalculationExpressionCmsMediabridgeFetchSingleCurrencyPortalCurrency,
    PropertyCalculationExpressionCmsMediabridgeDatedExchangeRate,
    PropertyCalculationExpressionCmsMediabridgePipelineProbability,
    PropertyCalculationExpressionCmsMediabridgeMaxNumbers,
    PropertyCalculationExpressionCmsMediabridgeMinNumbers,
    PropertyCalculationExpressionCmsMediabridgeLessThan,
    PropertyCalculationExpressionCmsMediabridgeLessThanOrEqual,
    PropertyCalculationExpressionCmsMediabridgeMoreThan,
    PropertyCalculationExpressionCmsMediabridgeMoreThanOrEqual,
    PropertyCalculationExpressionCmsMediabridgeNumberEquals,
    PropertyCalculationExpressionCmsMediabridgeStringEquals,
    PropertyCalculationExpressionCmsMediabridgeIsPipelineStageClosed,
    PropertyCalculationExpressionCmsMediabridgeNot,
    PropertyCalculationExpressionCmsMediabridgeDate,
    PropertyCalculationExpressionCmsMediabridgeMonth,
    PropertyCalculationExpressionCmsMediabridgeYear,
    PropertyCalculationExpressionCmsMediabridgeNow,
    PropertyCalculationExpressionCmsMediabridgeTimeBetween,
    PropertyCalculationExpressionCmsMediabridgePeriodToMonths,
    PropertyCalculationExpressionCmsMediabridgePeriodToWeeks,
    PropertyCalculationExpressionCmsMediabridgeAnd,
    PropertyCalculationExpressionCmsMediabridgeOr,
    PropertyCalculationExpressionCmsMediabridgeXor,
    PropertyCalculationExpressionCmsMediabridgeIfString,
    PropertyCalculationExpressionCmsMediabridgeIfNumber,
    PropertyCalculationExpressionCmsMediabridgeIfBoolean,
    PropertyCalculationExpressionCmsMediabridgeIsPresent,
    PropertyCalculationExpressionCmsMediabridgeHasEmailReply,
    PropertyCalculationExpressionCmsMediabridgeHasPlainTextEmailReply,
    PropertyCalculationExpressionCmsMediabridgeExtractMostRecentEmailReplyHTML,
    PropertyCalculationExpressionCmsMediabridgeExtractMostRecentEmailReplyText,
    PropertyCalculationExpressionCmsMediabridgeExtractMostRecentPlainTextEmailReply,
    PropertyCalculationExpressionCmsMediabridgeSetContainsString,
    PropertyCalculationExpressionCmsMediabridgeIsEngagementType,
    PropertyCalculationExpressionCmsMediabridgeFormatFullName,
    PropertyCalculationExpressionCmsMediabridgeAbsoluteValue,
    PropertyCalculationExpressionCmsMediabridgeSquareRoot,
    PropertyCalculationExpressionCmsMediabridgePower,
    PropertyCalculationExpressionCmsMediabridgeSubstring,
    PropertyCalculationExpressionCmsMediabridgeEuler,
    PropertyCalculationExpressionCmsMediabridgeStringLength,
    PropertyCalculationExpressionCmsMediabridgeAddTime,
    PropertyCalculationExpressionCmsMediabridgeSubtractTime,
]


class PropertyDefinitionSource(BaseModel):
    type: Literal["GLOBAL", "OBJECT_TYPE", "HAVEN_BRANCH", "PORTAL"]

    name: Optional[str] = None


class PropertyExtensionDataCaseChangeTestExtensionData(BaseModel):
    mood: str


class PropertyExtensionDataOptionDecoratorsExtensionDataOptionDecorators(BaseModel):
    color: str


class PropertyExtensionDataOptionDecoratorsExtensionData(BaseModel):
    option_decorators: Dict[str, PropertyExtensionDataOptionDecoratorsExtensionDataOptionDecorators] = FieldInfo(
        alias="optionDecorators"
    )

    option_decorator_style: str = FieldInfo(alias="optionDecoratorStyle")


class PropertyExtensionDataRequiredPropertiesExtensionData(BaseModel):
    is_required_property: bool = FieldInfo(alias="isRequiredProperty")


class PropertyExtensionDataSoftRequiredPropertiesExtensionData(BaseModel):
    is_soft_required_property: bool = FieldInfo(alias="isSoftRequiredProperty")


class PropertyExtensionData(BaseModel):
    extension_status_map: Dict[str, str] = FieldInfo(alias="extensionStatusMap")

    tags: List[str]

    case_change_test_extension_data: Optional[PropertyExtensionDataCaseChangeTestExtensionData] = FieldInfo(
        alias="caseChangeTestExtensionData", default=None
    )

    option_decorators_extension_data: Optional[PropertyExtensionDataOptionDecoratorsExtensionData] = FieldInfo(
        alias="optionDecoratorsExtensionData", default=None
    )

    required_properties_extension_data: Optional[PropertyExtensionDataRequiredPropertiesExtensionData] = FieldInfo(
        alias="requiredPropertiesExtensionData", default=None
    )

    soft_required_properties_extension_data: Optional[PropertyExtensionDataSoftRequiredPropertiesExtensionData] = (
        FieldInfo(alias="softRequiredPropertiesExtensionData", default=None)
    )


class PropertyExternalOptionsMetaDataFilter(BaseModel):
    include_unconfirmed_users: bool = FieldInfo(alias="includeUnconfirmedUsers")

    pipeline_ids: List[str] = FieldInfo(alias="pipelineIds")


class PropertyExternalOptionsMetaData(BaseModel):
    filter: Optional[PropertyExternalOptionsMetaDataFilter] = None

    related_object_type_id: Optional[str] = FieldInfo(alias="relatedObjectTypeId", default=None)


class PropertyPermission(BaseModel):
    access_level: str = FieldInfo(alias="accessLevel")


class PropertyPropertyDefinitionSource(BaseModel):
    type: str

    name: Optional[str] = None


class PropertyPropertyRequirements(BaseModel):
    gates: List[str]

    operator: Literal["AND", "OR"]

    scope_names: List[str] = FieldInfo(alias="scopeNames")

    settings: List[str]


class PropertyRollupExpressionConditionalExpressionCmsMediabridgeConstantBoolean(BaseModel):
    operator: Literal["CONSTANT_BOOLEAN"]

    inputs: Optional[List[object]] = None

    property_name: Optional[str] = FieldInfo(alias="propertyName", default=None)

    value: Optional[bool] = None


class PropertyRollupExpressionConditionalExpressionCmsMediabridgeConstantNumber(BaseModel):
    operator: Literal["CONSTANT_NUMBER"]

    inputs: Optional[List[object]] = None

    property_name: Optional[str] = FieldInfo(alias="propertyName", default=None)

    value: Optional[float] = None


class PropertyRollupExpressionConditionalExpressionCmsMediabridgeConstantString(BaseModel):
    operator: Literal["CONSTANT_STRING"]

    inputs: Optional[List[object]] = None

    property_name: Optional[str] = FieldInfo(alias="propertyName", default=None)

    value: Optional[str] = None


class PropertyRollupExpressionConditionalExpressionCmsMediabridgeBooleanPropertyVariable(BaseModel):
    operator: Literal["BOOLEAN_PROPERTY_VARIABLE"]

    inputs: Optional[List[object]] = None

    property_name: Optional[str] = FieldInfo(alias="propertyName", default=None)

    value: Optional[bool] = None


class PropertyRollupExpressionConditionalExpressionCmsMediabridgeStringPropertyVariable(BaseModel):
    operator: Literal["STRING_PROPERTY_VARIABLE"]

    inputs: Optional[List[object]] = None

    property_name: Optional[str] = FieldInfo(alias="propertyName", default=None)

    value: Optional[str] = None


class PropertyRollupExpressionConditionalExpressionCmsMediabridgeNumberPropertyVariable(BaseModel):
    operator: Literal["NUMBER_PROPERTY_VARIABLE"]

    inputs: Optional[List[object]] = None

    property_name: Optional[str] = FieldInfo(alias="propertyName", default=None)

    value: Optional[float] = None


class PropertyRollupExpressionConditionalExpressionCmsMediabridgeTimestampOfPropertyVariable(BaseModel):
    operator: Literal["TIMESTAMP_OF_PROPERTY_VARIABLE"]

    inputs: Optional[List[object]] = None

    property_name: Optional[str] = FieldInfo(alias="propertyName", default=None)

    value: Optional[str] = None


class PropertyRollupExpressionConditionalExpressionCmsMediabridgeBooleanTargetPropertyVariable(BaseModel):
    operator: Literal["BOOLEAN_TARGET_PROPERTY_VARIABLE"]

    inputs: Optional[List[object]] = None

    property_name: Optional[str] = FieldInfo(alias="propertyName", default=None)

    value: Optional[bool] = None


class PropertyRollupExpressionConditionalExpressionCmsMediabridgeStringTargetPropertyVariable(BaseModel):
    operator: Literal["STRING_TARGET_PROPERTY_VARIABLE"]

    inputs: Optional[List[object]] = None

    property_name: Optional[str] = FieldInfo(alias="propertyName", default=None)

    value: Optional[str] = None


class PropertyRollupExpressionConditionalExpressionCmsMediabridgeNumberTargetPropertyVariable(BaseModel):
    operator: Literal["NUMBER_TARGET_PROPERTY_VARIABLE"]

    inputs: Optional[List[object]] = None

    property_name: Optional[str] = FieldInfo(alias="propertyName", default=None)

    value: Optional[float] = None


class PropertyRollupExpressionConditionalExpressionCmsMediabridgeTimestampOfTargetPropertyVariable(BaseModel):
    operator: Literal["TIMESTAMP_OF_TARGET_PROPERTY_VARIABLE"]

    inputs: Optional[List[object]] = None

    property_name: Optional[str] = FieldInfo(alias="propertyName", default=None)

    value: Optional[str] = None


class PropertyRollupExpressionConditionalExpressionCmsMediabridgeAddNumbers(BaseModel):
    enclosed_in_parentheses: bool = FieldInfo(alias="enclosedInParentheses")

    operator: Literal["ADD_NUMBERS"]

    inputs: Optional[List[object]] = None

    property_name: Optional[str] = FieldInfo(alias="propertyName", default=None)

    value: Optional[float] = None


class PropertyRollupExpressionConditionalExpressionCmsMediabridgeSubtractNumbers(BaseModel):
    enclosed_in_parentheses: bool = FieldInfo(alias="enclosedInParentheses")

    operator: Literal["SUBTRACT_NUMBERS"]

    inputs: Optional[List[object]] = None

    property_name: Optional[str] = FieldInfo(alias="propertyName", default=None)

    value: Optional[float] = None


class PropertyRollupExpressionConditionalExpressionCmsMediabridgeMultiplyNumbers(BaseModel):
    enclosed_in_parentheses: bool = FieldInfo(alias="enclosedInParentheses")

    operator: Literal["MULTIPLY_NUMBERS"]

    inputs: Optional[List[object]] = None

    property_name: Optional[str] = FieldInfo(alias="propertyName", default=None)

    value: Optional[float] = None


class PropertyRollupExpressionConditionalExpressionCmsMediabridgeDivideNumbers(BaseModel):
    enclosed_in_parentheses: bool = FieldInfo(alias="enclosedInParentheses")

    operator: Literal["DIVIDE_NUMBERS"]

    inputs: Optional[List[object]] = None

    property_name: Optional[str] = FieldInfo(alias="propertyName", default=None)

    value: Optional[float] = None


class PropertyRollupExpressionConditionalExpressionCmsMediabridgeRoundDownNumbers(BaseModel):
    operator: Literal["ROUND_DOWN"]

    inputs: Optional[List[object]] = None

    property_name: Optional[str] = FieldInfo(alias="propertyName", default=None)

    value: Optional[float] = None


class PropertyRollupExpressionConditionalExpressionCmsMediabridgeRoundUpNumbers(BaseModel):
    operator: Literal["ROUND_UP"]

    inputs: Optional[List[object]] = None

    property_name: Optional[str] = FieldInfo(alias="propertyName", default=None)

    value: Optional[float] = None


class PropertyRollupExpressionConditionalExpressionCmsMediabridgeRoundNearestNumbers(BaseModel):
    operator: Literal["ROUND_NEAREST"]

    inputs: Optional[List[object]] = None

    property_name: Optional[str] = FieldInfo(alias="propertyName", default=None)

    value: Optional[float] = None


class PropertyRollupExpressionConditionalExpressionCmsMediabridgeUpperCase(BaseModel):
    operator: Literal["UPPER_CASE"]

    inputs: Optional[List[object]] = None

    property_name: Optional[str] = FieldInfo(alias="propertyName", default=None)

    value: Optional[str] = None


class PropertyRollupExpressionConditionalExpressionCmsMediabridgeLowerCase(BaseModel):
    operator: Literal["LOWER_CASE"]

    inputs: Optional[List[object]] = None

    property_name: Optional[str] = FieldInfo(alias="propertyName", default=None)

    value: Optional[str] = None


class PropertyRollupExpressionConditionalExpressionCmsMediabridgeConcatStrings(BaseModel):
    operator: Literal["CONCAT_STRINGS"]

    inputs: Optional[List[object]] = None

    property_name: Optional[str] = FieldInfo(alias="propertyName", default=None)

    value: Optional[str] = None


class PropertyRollupExpressionConditionalExpressionCmsMediabridgeContains(BaseModel):
    operator: Literal["CONTAINS"]

    string_to_check: object = FieldInfo(alias="stringToCheck")

    inputs: Optional[List[object]] = None

    property_name: Optional[str] = FieldInfo(alias="propertyName", default=None)

    value: Optional[bool] = None


class PropertyRollupExpressionConditionalExpressionCmsMediabridgeBeginsWith(BaseModel):
    operator: Literal["BEGINS_WITH"]

    string_to_check: object = FieldInfo(alias="stringToCheck")

    inputs: Optional[List[object]] = None

    property_name: Optional[str] = FieldInfo(alias="propertyName", default=None)

    value: Optional[bool] = None


class PropertyRollupExpressionConditionalExpressionCmsMediabridgeNumberToString(BaseModel):
    operator: Literal["NUMBER_TO_STRING"]

    inputs: Optional[List[object]] = None

    property_name: Optional[str] = FieldInfo(alias="propertyName", default=None)

    value: Optional[str] = None


class PropertyRollupExpressionConditionalExpressionCmsMediabridgeParseNumber(BaseModel):
    operator: Literal["PARSE_NUMBER"]

    inputs: Optional[List[object]] = None

    property_name: Optional[str] = FieldInfo(alias="propertyName", default=None)

    value: Optional[float] = None


class PropertyRollupExpressionConditionalExpressionCmsMediabridgeFetchExchangeRate(BaseModel):
    operator: Literal["FETCH_EXCHANGE_RATE"]

    inputs: Optional[List[object]] = None

    property_name: Optional[str] = FieldInfo(alias="propertyName", default=None)

    value: Optional[float] = None


class PropertyRollupExpressionConditionalExpressionCmsMediabridgeFetchCurrencyDecimalPlaces(BaseModel):
    operator: Literal["FETCH_CURRENCY_DECIMAL_PLACES"]

    inputs: Optional[List[object]] = None

    property_name: Optional[str] = FieldInfo(alias="propertyName", default=None)

    value: Optional[float] = None


class PropertyRollupExpressionConditionalExpressionCmsMediabridgeFetchSingleCurrencyPortalCurrency(BaseModel):
    operator: Literal["FETCH_SINGLE_CURRENCY_PORTAL_CURRENCY"]

    inputs: Optional[List[object]] = None

    property_name: Optional[str] = FieldInfo(alias="propertyName", default=None)

    value: Optional[str] = None


class PropertyRollupExpressionConditionalExpressionCmsMediabridgeDatedExchangeRate(BaseModel):
    operator: Literal["DATED_EXCHANGE_RATE"]

    inputs: Optional[List[object]] = None

    property_name: Optional[str] = FieldInfo(alias="propertyName", default=None)

    value: Optional[float] = None


class PropertyRollupExpressionConditionalExpressionCmsMediabridgePipelineProbability(BaseModel):
    operator: Literal["PIPELINE_PROBABILITY"]

    inputs: Optional[List[object]] = None

    property_name: Optional[str] = FieldInfo(alias="propertyName", default=None)

    value: Optional[float] = None


class PropertyRollupExpressionConditionalExpressionCmsMediabridgeMaxNumbers(BaseModel):
    operator: Literal["MAX_NUMBERS"]

    inputs: Optional[List[object]] = None

    property_name: Optional[str] = FieldInfo(alias="propertyName", default=None)

    value: Optional[float] = None


class PropertyRollupExpressionConditionalExpressionCmsMediabridgeMinNumbers(BaseModel):
    operator: Literal["MIN_NUMBERS"]

    inputs: Optional[List[object]] = None

    property_name: Optional[str] = FieldInfo(alias="propertyName", default=None)

    value: Optional[float] = None


class PropertyRollupExpressionConditionalExpressionCmsMediabridgeLessThan(BaseModel):
    operator: Literal["LESS_THAN"]

    inputs: Optional[List[object]] = None

    property_name: Optional[str] = FieldInfo(alias="propertyName", default=None)

    value: Optional[bool] = None


class PropertyRollupExpressionConditionalExpressionCmsMediabridgeLessThanOrEqual(BaseModel):
    operator: Literal["LESS_THAN_OR_EQUAL"]

    inputs: Optional[List[object]] = None

    property_name: Optional[str] = FieldInfo(alias="propertyName", default=None)

    value: Optional[bool] = None


class PropertyRollupExpressionConditionalExpressionCmsMediabridgeMoreThan(BaseModel):
    operator: Literal["MORE_THAN"]

    inputs: Optional[List[object]] = None

    property_name: Optional[str] = FieldInfo(alias="propertyName", default=None)

    value: Optional[bool] = None


class PropertyRollupExpressionConditionalExpressionCmsMediabridgeMoreThanOrEqual(BaseModel):
    operator: Literal["MORE_THAN_OR_EQUAL"]

    inputs: Optional[List[object]] = None

    property_name: Optional[str] = FieldInfo(alias="propertyName", default=None)

    value: Optional[bool] = None


class PropertyRollupExpressionConditionalExpressionCmsMediabridgeNumberEquals(BaseModel):
    operator: Literal["NUMBER_EQUALS"]

    inputs: Optional[List[object]] = None

    property_name: Optional[str] = FieldInfo(alias="propertyName", default=None)

    value: Optional[bool] = None


class PropertyRollupExpressionConditionalExpressionCmsMediabridgeStringEquals(BaseModel):
    operator: Literal["STRING_EQUALS"]

    inputs: Optional[List[object]] = None

    property_name: Optional[str] = FieldInfo(alias="propertyName", default=None)

    value: Optional[bool] = None


class PropertyRollupExpressionConditionalExpressionCmsMediabridgeIsPipelineStageClosed(BaseModel):
    operator: Literal["IS_PIPELINE_STAGE_CLOSED"]

    inputs: Optional[List[object]] = None

    property_name: Optional[str] = FieldInfo(alias="propertyName", default=None)

    value: Optional[bool] = None


class PropertyRollupExpressionConditionalExpressionCmsMediabridgeNot(BaseModel):
    operator: Literal["NOT"]

    inputs: Optional[List[object]] = None

    property_name: Optional[str] = FieldInfo(alias="propertyName", default=None)

    value: Optional[bool] = None


class PropertyRollupExpressionConditionalExpressionCmsMediabridgeDate(BaseModel):
    operator: Literal["DATE"]

    inputs: Optional[List[object]] = None

    property_name: Optional[str] = FieldInfo(alias="propertyName", default=None)

    value: Optional[float] = None


class PropertyRollupExpressionConditionalExpressionCmsMediabridgeMonth(BaseModel):
    operator: Literal["MONTH"]

    inputs: Optional[List[object]] = None

    property_name: Optional[str] = FieldInfo(alias="propertyName", default=None)

    value: Optional[float] = None


class PropertyRollupExpressionConditionalExpressionCmsMediabridgeYear(BaseModel):
    operator: Literal["YEAR"]

    inputs: Optional[List[object]] = None

    property_name: Optional[str] = FieldInfo(alias="propertyName", default=None)

    value: Optional[float] = None


class PropertyRollupExpressionConditionalExpressionCmsMediabridgeNow(BaseModel):
    operator: Literal["NOW"]

    inputs: Optional[List[object]] = None

    property_name: Optional[str] = FieldInfo(alias="propertyName", default=None)

    value: Optional[float] = None


class PropertyRollupExpressionConditionalExpressionCmsMediabridgeTimeBetween(BaseModel):
    operator: Literal["TIME_BETWEEN"]

    inputs: Optional[List[object]] = None

    property_name: Optional[str] = FieldInfo(alias="propertyName", default=None)

    value: Optional[float] = None


class PropertyRollupExpressionConditionalExpressionCmsMediabridgePeriodToMonths(BaseModel):
    operator: Literal["PERIOD_TO_MONTHS"]

    inputs: Optional[List[object]] = None

    property_name: Optional[str] = FieldInfo(alias="propertyName", default=None)

    value: Optional[float] = None


class PropertyRollupExpressionConditionalExpressionCmsMediabridgePeriodToWeeks(BaseModel):
    operator: Literal["PERIOD_TO_WEEKS"]

    inputs: Optional[List[object]] = None

    property_name: Optional[str] = FieldInfo(alias="propertyName", default=None)

    value: Optional[float] = None


class PropertyRollupExpressionConditionalExpressionCmsMediabridgeAnd(BaseModel):
    enclosed_in_parentheses: bool = FieldInfo(alias="enclosedInParentheses")

    operator: Literal["AND"]

    inputs: Optional[List[object]] = None

    property_name: Optional[str] = FieldInfo(alias="propertyName", default=None)

    value: Optional[bool] = None


class PropertyRollupExpressionConditionalExpressionCmsMediabridgeOr(BaseModel):
    enclosed_in_parentheses: bool = FieldInfo(alias="enclosedInParentheses")

    operator: Literal["OR"]

    inputs: Optional[List[object]] = None

    property_name: Optional[str] = FieldInfo(alias="propertyName", default=None)

    value: Optional[bool] = None


class PropertyRollupExpressionConditionalExpressionCmsMediabridgeXor(BaseModel):
    enclosed_in_parentheses: bool = FieldInfo(alias="enclosedInParentheses")

    operator: Literal["XOR"]

    inputs: Optional[List[object]] = None

    property_name: Optional[str] = FieldInfo(alias="propertyName", default=None)

    value: Optional[bool] = None


class PropertyRollupExpressionConditionalExpressionCmsMediabridgeIfString(BaseModel):
    enclosed_in_parentheses: bool = FieldInfo(alias="enclosedInParentheses")

    if_expression: object = FieldInfo(alias="ifExpression")

    operator: Literal["IF_STRING"]

    else_expression: Optional[object] = FieldInfo(alias="elseExpression", default=None)

    inputs: Optional[List[object]] = None

    property_name: Optional[str] = FieldInfo(alias="propertyName", default=None)

    value: Optional[str] = None


class PropertyRollupExpressionConditionalExpressionCmsMediabridgeIfNumber(BaseModel):
    enclosed_in_parentheses: bool = FieldInfo(alias="enclosedInParentheses")

    if_expression: object = FieldInfo(alias="ifExpression")

    operator: Literal["IF_NUMBER"]

    else_expression: Optional[object] = FieldInfo(alias="elseExpression", default=None)

    inputs: Optional[List[object]] = None

    property_name: Optional[str] = FieldInfo(alias="propertyName", default=None)

    value: Optional[float] = None


class PropertyRollupExpressionConditionalExpressionCmsMediabridgeIfBoolean(BaseModel):
    enclosed_in_parentheses: bool = FieldInfo(alias="enclosedInParentheses")

    if_expression: object = FieldInfo(alias="ifExpression")

    operator: Literal["IF_BOOLEAN"]

    else_expression: Optional[object] = FieldInfo(alias="elseExpression", default=None)

    inputs: Optional[List[object]] = None

    property_name: Optional[str] = FieldInfo(alias="propertyName", default=None)

    value: Optional[bool] = None


class PropertyRollupExpressionConditionalExpressionCmsMediabridgeIsPresent(BaseModel):
    expression_to_evaluate: object = FieldInfo(alias="expressionToEvaluate")

    operator: Literal["IS_PRESENT"]

    inputs: Optional[List[object]] = None

    property_name: Optional[str] = FieldInfo(alias="propertyName", default=None)

    value: Optional[bool] = None


class PropertyRollupExpressionConditionalExpressionCmsMediabridgeHasEmailReply(BaseModel):
    operator: Literal["HAS_EMAIL_REPLY"]

    inputs: Optional[List[object]] = None

    property_name: Optional[str] = FieldInfo(alias="propertyName", default=None)

    value: Optional[bool] = None


class PropertyRollupExpressionConditionalExpressionCmsMediabridgeHasPlainTextEmailReply(BaseModel):
    operator: Literal["HAS_PLAIN_TEXT_EMAIL_REPLY"]

    inputs: Optional[List[object]] = None

    property_name: Optional[str] = FieldInfo(alias="propertyName", default=None)

    value: Optional[bool] = None


class PropertyRollupExpressionConditionalExpressionCmsMediabridgeExtractMostRecentEmailReplyHTML(BaseModel):
    operator: Literal["EXTRACT_MOST_RECENT_EMAIL_REPLY_HTML"]

    inputs: Optional[List[object]] = None

    property_name: Optional[str] = FieldInfo(alias="propertyName", default=None)

    value: Optional[str] = None


class PropertyRollupExpressionConditionalExpressionCmsMediabridgeExtractMostRecentEmailReplyText(BaseModel):
    operator: Literal["EXTRACT_MOST_RECENT_EMAIL_REPLY_TEXT"]

    inputs: Optional[List[object]] = None

    property_name: Optional[str] = FieldInfo(alias="propertyName", default=None)

    value: Optional[str] = None


class PropertyRollupExpressionConditionalExpressionCmsMediabridgeExtractMostRecentPlainTextEmailReply(BaseModel):
    operator: Literal["EXTRACT_MOST_RECENT_PLAIN_TEXT_EMAIL_REPLY"]

    inputs: Optional[List[object]] = None

    property_name: Optional[str] = FieldInfo(alias="propertyName", default=None)

    value: Optional[str] = None


class PropertyRollupExpressionConditionalExpressionCmsMediabridgeSetContainsString(BaseModel):
    operator: Literal["SET_CONTAINS_STRING"]

    string_to_check: object = FieldInfo(alias="stringToCheck")

    inputs: Optional[List[object]] = None

    property_name: Optional[str] = FieldInfo(alias="propertyName", default=None)

    value: Optional[bool] = None


class PropertyRollupExpressionConditionalExpressionCmsMediabridgeIsEngagementType(BaseModel):
    operator: Literal["IS_ENGAGEMENT_TYPE"]

    inputs: Optional[List[object]] = None

    property_name: Optional[str] = FieldInfo(alias="propertyName", default=None)

    value: Optional[bool] = None


class PropertyRollupExpressionConditionalExpressionCmsMediabridgeFormatFullName(BaseModel):
    operator: Literal["FORMAT_FULL_NAME"]

    inputs: Optional[List[object]] = None

    property_name: Optional[str] = FieldInfo(alias="propertyName", default=None)

    value: Optional[str] = None


class PropertyRollupExpressionConditionalExpressionCmsMediabridgeAbsoluteValue(BaseModel):
    operator: Literal["ABSOLUTE_VALUE"]

    inputs: Optional[List[object]] = None

    property_name: Optional[str] = FieldInfo(alias="propertyName", default=None)

    value: Optional[float] = None


class PropertyRollupExpressionConditionalExpressionCmsMediabridgeSquareRoot(BaseModel):
    operator: Literal["SQUARE_ROOT"]

    inputs: Optional[List[object]] = None

    property_name: Optional[str] = FieldInfo(alias="propertyName", default=None)

    value: Optional[float] = None


class PropertyRollupExpressionConditionalExpressionCmsMediabridgePower(BaseModel):
    operator: Literal["POWER"]

    inputs: Optional[List[object]] = None

    property_name: Optional[str] = FieldInfo(alias="propertyName", default=None)

    value: Optional[float] = None


class PropertyRollupExpressionConditionalExpressionCmsMediabridgeSubstring(BaseModel):
    operator: Literal["SUBSTRING"]

    string_to_check: object = FieldInfo(alias="stringToCheck")

    inputs: Optional[List[object]] = None

    property_name: Optional[str] = FieldInfo(alias="propertyName", default=None)

    value: Optional[str] = None


class PropertyRollupExpressionConditionalExpressionCmsMediabridgeEuler(BaseModel):
    operator: Literal["EULER"]

    inputs: Optional[List[object]] = None

    property_name: Optional[str] = FieldInfo(alias="propertyName", default=None)

    value: Optional[float] = None


class PropertyRollupExpressionConditionalExpressionCmsMediabridgeStringLength(BaseModel):
    operator: Literal["STRING_LENGTH"]

    inputs: Optional[List[object]] = None

    property_name: Optional[str] = FieldInfo(alias="propertyName", default=None)

    value: Optional[float] = None


class PropertyRollupExpressionConditionalExpressionCmsMediabridgeAddTime(BaseModel):
    operator: Literal["ADD_TIME"]

    string_to_check: object = FieldInfo(alias="stringToCheck")

    inputs: Optional[List[object]] = None

    property_name: Optional[str] = FieldInfo(alias="propertyName", default=None)

    value: Optional[float] = None


class PropertyRollupExpressionConditionalExpressionCmsMediabridgeSubtractTime(BaseModel):
    operator: Literal["SUBTRACT_TIME"]

    string_to_check: object = FieldInfo(alias="stringToCheck")

    inputs: Optional[List[object]] = None

    property_name: Optional[str] = FieldInfo(alias="propertyName", default=None)

    value: Optional[float] = None


PropertyRollupExpressionConditionalExpression: TypeAlias = Union[
    PropertyRollupExpressionConditionalExpressionCmsMediabridgeConstantBoolean,
    PropertyRollupExpressionConditionalExpressionCmsMediabridgeConstantNumber,
    PropertyRollupExpressionConditionalExpressionCmsMediabridgeConstantString,
    PropertyRollupExpressionConditionalExpressionCmsMediabridgeBooleanPropertyVariable,
    PropertyRollupExpressionConditionalExpressionCmsMediabridgeStringPropertyVariable,
    PropertyRollupExpressionConditionalExpressionCmsMediabridgeNumberPropertyVariable,
    PropertyRollupExpressionConditionalExpressionCmsMediabridgeTimestampOfPropertyVariable,
    PropertyRollupExpressionConditionalExpressionCmsMediabridgeBooleanTargetPropertyVariable,
    PropertyRollupExpressionConditionalExpressionCmsMediabridgeStringTargetPropertyVariable,
    PropertyRollupExpressionConditionalExpressionCmsMediabridgeNumberTargetPropertyVariable,
    PropertyRollupExpressionConditionalExpressionCmsMediabridgeTimestampOfTargetPropertyVariable,
    PropertyRollupExpressionConditionalExpressionCmsMediabridgeAddNumbers,
    PropertyRollupExpressionConditionalExpressionCmsMediabridgeSubtractNumbers,
    PropertyRollupExpressionConditionalExpressionCmsMediabridgeMultiplyNumbers,
    PropertyRollupExpressionConditionalExpressionCmsMediabridgeDivideNumbers,
    PropertyRollupExpressionConditionalExpressionCmsMediabridgeRoundDownNumbers,
    PropertyRollupExpressionConditionalExpressionCmsMediabridgeRoundUpNumbers,
    PropertyRollupExpressionConditionalExpressionCmsMediabridgeRoundNearestNumbers,
    PropertyRollupExpressionConditionalExpressionCmsMediabridgeUpperCase,
    PropertyRollupExpressionConditionalExpressionCmsMediabridgeLowerCase,
    PropertyRollupExpressionConditionalExpressionCmsMediabridgeConcatStrings,
    PropertyRollupExpressionConditionalExpressionCmsMediabridgeContains,
    PropertyRollupExpressionConditionalExpressionCmsMediabridgeBeginsWith,
    PropertyRollupExpressionConditionalExpressionCmsMediabridgeNumberToString,
    PropertyRollupExpressionConditionalExpressionCmsMediabridgeParseNumber,
    PropertyRollupExpressionConditionalExpressionCmsMediabridgeFetchExchangeRate,
    PropertyRollupExpressionConditionalExpressionCmsMediabridgeFetchCurrencyDecimalPlaces,
    PropertyRollupExpressionConditionalExpressionCmsMediabridgeFetchSingleCurrencyPortalCurrency,
    PropertyRollupExpressionConditionalExpressionCmsMediabridgeDatedExchangeRate,
    PropertyRollupExpressionConditionalExpressionCmsMediabridgePipelineProbability,
    PropertyRollupExpressionConditionalExpressionCmsMediabridgeMaxNumbers,
    PropertyRollupExpressionConditionalExpressionCmsMediabridgeMinNumbers,
    PropertyRollupExpressionConditionalExpressionCmsMediabridgeLessThan,
    PropertyRollupExpressionConditionalExpressionCmsMediabridgeLessThanOrEqual,
    PropertyRollupExpressionConditionalExpressionCmsMediabridgeMoreThan,
    PropertyRollupExpressionConditionalExpressionCmsMediabridgeMoreThanOrEqual,
    PropertyRollupExpressionConditionalExpressionCmsMediabridgeNumberEquals,
    PropertyRollupExpressionConditionalExpressionCmsMediabridgeStringEquals,
    PropertyRollupExpressionConditionalExpressionCmsMediabridgeIsPipelineStageClosed,
    PropertyRollupExpressionConditionalExpressionCmsMediabridgeNot,
    PropertyRollupExpressionConditionalExpressionCmsMediabridgeDate,
    PropertyRollupExpressionConditionalExpressionCmsMediabridgeMonth,
    PropertyRollupExpressionConditionalExpressionCmsMediabridgeYear,
    PropertyRollupExpressionConditionalExpressionCmsMediabridgeNow,
    PropertyRollupExpressionConditionalExpressionCmsMediabridgeTimeBetween,
    PropertyRollupExpressionConditionalExpressionCmsMediabridgePeriodToMonths,
    PropertyRollupExpressionConditionalExpressionCmsMediabridgePeriodToWeeks,
    PropertyRollupExpressionConditionalExpressionCmsMediabridgeAnd,
    PropertyRollupExpressionConditionalExpressionCmsMediabridgeOr,
    PropertyRollupExpressionConditionalExpressionCmsMediabridgeXor,
    PropertyRollupExpressionConditionalExpressionCmsMediabridgeIfString,
    PropertyRollupExpressionConditionalExpressionCmsMediabridgeIfNumber,
    PropertyRollupExpressionConditionalExpressionCmsMediabridgeIfBoolean,
    PropertyRollupExpressionConditionalExpressionCmsMediabridgeIsPresent,
    PropertyRollupExpressionConditionalExpressionCmsMediabridgeHasEmailReply,
    PropertyRollupExpressionConditionalExpressionCmsMediabridgeHasPlainTextEmailReply,
    PropertyRollupExpressionConditionalExpressionCmsMediabridgeExtractMostRecentEmailReplyHTML,
    PropertyRollupExpressionConditionalExpressionCmsMediabridgeExtractMostRecentEmailReplyText,
    PropertyRollupExpressionConditionalExpressionCmsMediabridgeExtractMostRecentPlainTextEmailReply,
    PropertyRollupExpressionConditionalExpressionCmsMediabridgeSetContainsString,
    PropertyRollupExpressionConditionalExpressionCmsMediabridgeIsEngagementType,
    PropertyRollupExpressionConditionalExpressionCmsMediabridgeFormatFullName,
    PropertyRollupExpressionConditionalExpressionCmsMediabridgeAbsoluteValue,
    PropertyRollupExpressionConditionalExpressionCmsMediabridgeSquareRoot,
    PropertyRollupExpressionConditionalExpressionCmsMediabridgePower,
    PropertyRollupExpressionConditionalExpressionCmsMediabridgeSubstring,
    PropertyRollupExpressionConditionalExpressionCmsMediabridgeEuler,
    PropertyRollupExpressionConditionalExpressionCmsMediabridgeStringLength,
    PropertyRollupExpressionConditionalExpressionCmsMediabridgeAddTime,
    PropertyRollupExpressionConditionalExpressionCmsMediabridgeSubtractTime,
]


class PropertyRollupExpression(BaseModel):
    association_types: List[AssociationSpec] = FieldInfo(alias="associationTypes")

    rollup_operator: str = FieldInfo(alias="rollupOperator")

    source_object_type_id: str = FieldInfo(alias="sourceObjectTypeId")

    source_property_name: str = FieldInfo(alias="sourcePropertyName")

    conditional_expression: Optional[PropertyRollupExpressionConditionalExpression] = FieldInfo(
        alias="conditionalExpression", default=None
    )

    conditional_formula: Optional[str] = FieldInfo(alias="conditionalFormula", default=None)

    empty_rollup_value: Optional[str] = FieldInfo(alias="emptyRollupValue", default=None)

    source_compare_by_property_name: Optional[str] = FieldInfo(alias="sourceCompareByPropertyName", default=None)


class Property(BaseModel):
    object_type_id: str = FieldInfo(alias="objectTypeId")

    property: _property.Property
    """Defines a property"""

    calculation_expression: Optional[PropertyCalculationExpression] = FieldInfo(
        alias="calculationExpression", default=None
    )

    calculation_formula: Optional[str] = FieldInfo(alias="calculationFormula", default=None)

    definition_source: Optional[PropertyDefinitionSource] = FieldInfo(alias="definitionSource", default=None)

    extension_data: Optional[PropertyExtensionData] = FieldInfo(alias="extensionData", default=None)

    external_options_meta_data: Optional[PropertyExternalOptionsMetaData] = FieldInfo(
        alias="externalOptionsMetaData", default=None
    )

    fulcrum_portal_id: Optional[int] = FieldInfo(alias="fulcrumPortalId", default=None)

    fulcrum_timestamp: Optional[int] = FieldInfo(alias="fulcrumTimestamp", default=None)

    janus_group: Optional[str] = FieldInfo(alias="janusGroup", default=None)

    permission: Optional[PropertyPermission] = None

    property_definition_source: Optional[PropertyPropertyDefinitionSource] = FieldInfo(
        alias="propertyDefinitionSource", default=None
    )

    property_requirements: Optional[PropertyPropertyRequirements] = FieldInfo(
        alias="propertyRequirements", default=None
    )

    rollup_expression: Optional[PropertyRollupExpression] = FieldInfo(alias="rollupExpression", default=None)


class PropertyGroup(BaseModel):
    display_name: str = FieldInfo(alias="displayName")

    display_order: int = FieldInfo(alias="displayOrder")

    fulcrum_portal_id: int = FieldInfo(alias="fulcrumPortalId")

    fulcrum_timestamp: int = FieldInfo(alias="fulcrumTimestamp")

    hubspot_defined: bool = FieldInfo(alias="hubspotDefined")

    name: str


class SchemaScopeMapping(BaseModel):
    access_level: str = FieldInfo(alias="accessLevel")

    request_action: str = FieldInfo(alias="requestAction")

    scope_name: str = FieldInfo(alias="scopeName")


class Schema(BaseModel):
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

    scope_mappings: List[SchemaScopeMapping] = FieldInfo(alias="scopeMappings")

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


class IntegratorSettingGetObjectDefinitionsByMediaTypeResponse(BaseModel):
    object_type_id: str = FieldInfo(alias="objectTypeId")

    object_type_name: str = FieldInfo(alias="objectTypeName")

    properties: List[Property]

    property_groups: List[PropertyGroup] = FieldInfo(alias="propertyGroups")

    schema_: Optional[Schema] = FieldInfo(alias="schema", default=None)
