# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["PublicPropertyValidationRule"]


class PublicPropertyValidationRule(BaseModel):
    rule_arguments: List[str] = FieldInfo(alias="ruleArguments")
    """
    A list of arguments that define the specific conditions or parameters for the
    validation rule.
    """

    rule_type: Literal[
        "AFTER_DATETIME_DURATION",
        "AFTER_DURATION",
        "ALPHANUMERIC",
        "BEFORE_DATETIME_DURATION",
        "BEFORE_DURATION",
        "DAYS_OF_WEEK",
        "DECIMAL",
        "DOMAIN",
        "EMAIL",
        "EMAIL_ALLOWED_DOMAINS",
        "EMAIL_BLOCKED_DOMAINS",
        "END_DATE",
        "END_DATETIME",
        "FORMAT",
        "MAX_LENGTH",
        "MAX_NUMBER",
        "MIN_LENGTH",
        "MIN_NUMBER",
        "PHONE_NUMBER_WITH_EXPLICIT_COUNTRY_CODE",
        "REGEX",
        "SPECIAL_CHARACTERS",
        "START_DATE",
        "START_DATETIME",
        "URL",
        "URL_ALLOWED_DOMAINS",
        "URL_BLOCKED_DOMAINS",
        "WHITESPACE",
    ] = FieldInfo(alias="ruleType")
    """
    The category of validation applied to the property, such as FORMAT,
    ALPHANUMERIC, or MAX_LENGTH.
    """
