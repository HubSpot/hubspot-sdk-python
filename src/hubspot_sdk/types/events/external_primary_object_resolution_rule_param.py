# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["ExternalPrimaryObjectResolutionRuleParam"]


class ExternalPrimaryObjectResolutionRuleParam(TypedDict, total=False):
    event_property_name: Required[Annotated[str, PropertyInfo(alias="eventPropertyName")]]

    target_object_property_name: Required[Annotated[str, PropertyInfo(alias="targetObjectPropertyName")]]
