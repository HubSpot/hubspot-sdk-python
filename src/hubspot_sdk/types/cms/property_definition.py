# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from typing_extensions import TypeAlias

from pydantic import Field as FieldInfo

from .now import Now
from .euler import Euler
from .property import Property
from ..._models import BaseModel
from .extension_data import ExtensionData
from .constant_number import ConstantNumber
from .constant_string import ConstantString
from .constant_boolean import ConstantBoolean
from .definition_source import DefinitionSource
from .is_engagement_type import IsEngagementType
from .default_requirements import DefaultRequirements
from .field_level_permission import FieldLevelPermission
from .number_property_variable import NumberPropertyVariable
from .string_property_variable import StringPropertyVariable
from .boolean_property_variable import BooleanPropertyVariable
from .external_options_meta_data import ExternalOptionsMetaData
from .property_definition_source import PropertyDefinitionSource
from .timestamp_of_property_variable import TimestampOfPropertyVariable
from .number_target_property_variable import NumberTargetPropertyVariable
from .string_target_property_variable import StringTargetPropertyVariable
from .boolean_target_property_variable import BooleanTargetPropertyVariable
from .fetch_single_currency_portal_currency import FetchSingleCurrencyPortalCurrency
from .timestamp_of_target_property_variable import TimestampOfTargetPropertyVariable

__all__ = ["PropertyDefinition", "CalculationExpression"]

CalculationExpression: TypeAlias = Union[
    ConstantBoolean,
    ConstantNumber,
    ConstantString,
    BooleanPropertyVariable,
    StringPropertyVariable,
    NumberPropertyVariable,
    TimestampOfPropertyVariable,
    BooleanTargetPropertyVariable,
    StringTargetPropertyVariable,
    NumberTargetPropertyVariable,
    TimestampOfTargetPropertyVariable,
    "AddNumbers",
    "SubtractNumbers",
    "MultiplyNumbers",
    "DivideNumbers",
    "RoundDownNumbers",
    "RoundUpNumbers",
    "RoundNearestNumbers",
    "UpperCase",
    "LowerCase",
    "ConcatStrings",
    "Contains",
    "BeginsWith",
    "NumberToString",
    "ParseNumber",
    "FetchExchangeRate",
    "FetchCurrencyDecimalPlaces",
    FetchSingleCurrencyPortalCurrency,
    "DatedExchangeRate",
    "PipelineProbability",
    "MaxNumbers",
    "MinNumbers",
    "LessThan",
    "LessThanOrEqual",
    "MoreThan",
    "MoreThanOrEqual",
    "NumberEquals",
    "StringEquals",
    "IsPipelineStageClosed",
    "Not",
    "Date",
    "Month",
    "Year",
    Now,
    "TimeBetween",
    "TimeBetweenSkipWeekends",
    "PeriodToMonths",
    "PeriodToWeeks",
    "And",
    "Or",
    "Xor",
    "IfString",
    "IfNumber",
    "IfBoolean",
    "IsPresent",
    "HasEmailReply",
    "HasPlainTextEmailReply",
    "ExtractMostRecentEmailReplyHTML",
    "ExtractMostRecentEmailReplyText",
    "ExtractMostRecentPlainTextEmailReply",
    "SetContainsString",
    IsEngagementType,
    "FormatFullName",
    "FormatPhoneNumber",
    "FormatSearchablePhoneNumber",
    "AbsoluteValue",
    "SquareRoot",
    "Power",
    "Substring",
    Euler,
    "StringLength",
    "IsBlank",
    "AddTime",
    "SubtractTime",
]


class PropertyDefinition(BaseModel):
    object_type_id: str = FieldInfo(alias="objectTypeId")

    property: Property
    """A HubSpot property"""

    calculation_expression: Optional[CalculationExpression] = FieldInfo(alias="calculationExpression", default=None)

    calculation_formula: Optional[str] = FieldInfo(alias="calculationFormula", default=None)

    definition_source: Optional[PropertyDefinitionSource] = FieldInfo(alias="definitionSource", default=None)

    extension_data: Optional[ExtensionData] = FieldInfo(alias="extensionData", default=None)

    external_options_meta_data: Optional[ExternalOptionsMetaData] = FieldInfo(
        alias="externalOptionsMetaData", default=None
    )

    fulcrum_portal_id: Optional[int] = FieldInfo(alias="fulcrumPortalId", default=None)

    fulcrum_timestamp: Optional[int] = FieldInfo(alias="fulcrumTimestamp", default=None)

    janus_group: Optional[str] = FieldInfo(alias="janusGroup", default=None)

    permission: Optional[FieldLevelPermission] = None

    property_definition_source: Optional[DefinitionSource] = FieldInfo(alias="propertyDefinitionSource", default=None)

    property_requirements: Optional[DefaultRequirements] = FieldInfo(alias="propertyRequirements", default=None)

    rollup_expression: Optional["RollupExpression"] = FieldInfo(alias="rollupExpression", default=None)


from .or_ import Or
from .xor import Xor
from .and_ import And
from .date import Date
from .not_ import Not
from .year import Year
from .month import Month
from .power import Power
from .add_time import AddTime
from .contains import Contains
from .is_blank import IsBlank
from .if_number import IfNumber
from .if_string import IfString
from .less_than import LessThan
from .more_than import MoreThan
from .substring import Substring
from .if_boolean import IfBoolean
from .is_present import IsPresent
from .lower_case import LowerCase
from .upper_case import UpperCase
from .add_numbers import AddNumbers
from .begins_with import BeginsWith
from .max_numbers import MaxNumbers
from .min_numbers import MinNumbers
from .square_root import SquareRoot
from .parse_number import ParseNumber
from .time_between import TimeBetween
from .number_equals import NumberEquals
from .string_equals import StringEquals
from .string_length import StringLength
from .subtract_time import SubtractTime
from .absolute_value import AbsoluteValue
from .concat_strings import ConcatStrings
from .divide_numbers import DivideNumbers
from .has_email_reply import HasEmailReply
from .period_to_weeks import PeriodToWeeks
from .format_full_name import FormatFullName
from .multiply_numbers import MultiplyNumbers
from .number_to_string import NumberToString
from .period_to_months import PeriodToMonths
from .round_up_numbers import RoundUpNumbers
from .subtract_numbers import SubtractNumbers
from .rollup_expression import RollupExpression
from .less_than_or_equal import LessThanOrEqual
from .more_than_or_equal import MoreThanOrEqual
from .round_down_numbers import RoundDownNumbers
from .dated_exchange_rate import DatedExchangeRate
from .fetch_exchange_rate import FetchExchangeRate
from .format_phone_number import FormatPhoneNumber
from .set_contains_string import SetContainsString
from .pipeline_probability import PipelineProbability
from .round_nearest_numbers import RoundNearestNumbers
from .is_pipeline_stage_closed import IsPipelineStageClosed
from .has_plain_text_email_reply import HasPlainTextEmailReply
from .time_between_skip_weekends import TimeBetweenSkipWeekends
from .fetch_currency_decimal_places import FetchCurrencyDecimalPlaces
from .format_searchable_phone_number import FormatSearchablePhoneNumber
from .extract_most_recent_email_reply_html import ExtractMostRecentEmailReplyHTML
from .extract_most_recent_email_reply_text import ExtractMostRecentEmailReplyText
from .extract_most_recent_plain_text_email_reply import ExtractMostRecentPlainTextEmailReply
