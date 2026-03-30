# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["DefinitionListParams"]


class DefinitionListParams(TypedDict, total=False):
    business_unit_id: Annotated[int, PropertyInfo(alias="businessUnitId")]

    include_translations: Annotated[bool, PropertyInfo(alias="includeTranslations")]
