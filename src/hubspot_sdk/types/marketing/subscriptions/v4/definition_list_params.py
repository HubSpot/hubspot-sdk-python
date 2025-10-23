# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ....._utils import PropertyInfo

__all__ = ["DefinitionListParams"]


class DefinitionListParams(TypedDict, total=False):
    business_unit_id: Annotated[int, PropertyInfo(alias="businessUnitId")]
    """
    If you have the
    [business unit add-on](https://developers.hubspot.com/beta-docs/guides/api/settings/business-units-api),
    include this parameter to filter results by business unit ID. The default
    Account business unit will always use `0`.
    """

    include_translations: Annotated[bool, PropertyInfo(alias="includeTranslations")]
    """
    Set to `true` to return subscription translations associated with each
    definition.
    """
