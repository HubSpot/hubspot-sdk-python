# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["IntegratorSettingGetObjectDefinitionsByMediaTypeParams"]


class IntegratorSettingGetObjectDefinitionsByMediaTypeParams(TypedDict, total=False):
    app_id: Required[Annotated[int, PropertyInfo(alias="appId")]]

    include_full_definition: Annotated[bool, PropertyInfo(alias="includeFullDefinition")]
    """Include the full definition in the response."""
