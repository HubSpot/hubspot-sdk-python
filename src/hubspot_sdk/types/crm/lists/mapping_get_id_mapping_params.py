# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["MappingGetIDMappingParams"]


class MappingGetIDMappingParams(TypedDict, total=False):
    legacy_list_id: Annotated[str, PropertyInfo(alias="legacyListId")]
    """The legacy list id from lists v1 API."""
