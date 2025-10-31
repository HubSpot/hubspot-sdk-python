# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["PropertyValidationListResponse", "Result", "ResultPropertyValidationRule"]


class ResultPropertyValidationRule(BaseModel):
    rule_arguments: List[str] = FieldInfo(alias="ruleArguments")

    rule_type: str = FieldInfo(alias="ruleType")


class Result(BaseModel):
    property_name: str = FieldInfo(alias="propertyName")

    property_validation_rules: List[ResultPropertyValidationRule] = FieldInfo(alias="propertyValidationRules")


class PropertyValidationListResponse(BaseModel):
    results: List[Result]
