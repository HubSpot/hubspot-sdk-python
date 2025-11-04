# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["PublicPropertyValidationRule"]


class PublicPropertyValidationRule(BaseModel):
    rule_arguments: List[str] = FieldInfo(alias="ruleArguments")

    rule_type: Literal[
        "FORMAT",
        "ALPHANUMERIC",
        "MAX_LENGTH",
        "MIN_LENGTH",
        "MIN_NUMBER",
        "MAX_NUMBER",
        "START_DATE",
        "END_DATE",
        "SPECIAL_CHARACTERS",
        "WHITESPACE",
        "DECIMAL",
        "BEFORE_DURATION",
        "AFTER_DURATION",
        "DAYS_OF_WEEK",
        "REGEX",
        "START_DATETIME",
        "END_DATETIME",
        "BEFORE_DATETIME_DURATION",
        "AFTER_DATETIME_DURATION",
        "PHONE_NUMBER_WITH_EXPLICIT_COUNTRY_CODE",
        "URL",
        "URL_ALLOWED_DOMAINS",
        "URL_BLOCKED_DOMAINS",
        "EMAIL",
        "EMAIL_ALLOWED_DOMAINS",
        "EMAIL_BLOCKED_DOMAINS",
        "DOMAIN",
    ] = FieldInfo(alias="ruleType")
