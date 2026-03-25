# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo
from .external_primary_object_resolution_rule_param import ExternalPrimaryObjectResolutionRuleParam

__all__ = ["ExternalObjectResolutionMappingRequestParam"]


class ExternalObjectResolutionMappingRequestParam(TypedDict, total=False):
    primary_object_rule: Required[
        Annotated[ExternalPrimaryObjectResolutionRuleParam, PropertyInfo(alias="primaryObjectRule")]
    ]
