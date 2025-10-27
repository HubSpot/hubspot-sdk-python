# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .public_property_validation_rule import PublicPropertyValidationRule

__all__ = ["PublicPropertyValidationRuleMap"]


class PublicPropertyValidationRuleMap(BaseModel):
    property_name: str = FieldInfo(alias="propertyName")

    property_validation_rules: List[PublicPropertyValidationRule] = FieldInfo(alias="propertyValidationRules")
