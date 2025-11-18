# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo

__all__ = ["PropertyValidationCrmV3PropertyValidationsObjectTypeIDPropertyNameRuleTypeRuleTypeParams"]


class PropertyValidationCrmV3PropertyValidationsObjectTypeIDPropertyNameRuleTypeRuleTypeParams(TypedDict, total=False):
    object_type_id: Required[Annotated[str, PropertyInfo(alias="objectTypeId")]]

    property_name: Required[Annotated[str, PropertyInfo(alias="propertyName")]]

    rule_arguments: Required[Annotated[SequenceNotStr[str], PropertyInfo(alias="ruleArguments")]]
    """A list of arguments that define the constraints for the validation rule."""
