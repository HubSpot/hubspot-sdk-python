# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo

__all__ = ["PublicAdsSearchFilter"]


class PublicAdsSearchFilter(TypedDict, total=False):
    ad_network: Required[Annotated[str, PropertyInfo(alias="adNetwork")]]

    entity_type: Required[Annotated[str, PropertyInfo(alias="entityType")]]

    filter_type: Required[Annotated[Literal["ADS_SEARCH"], PropertyInfo(alias="filterType")]]

    operator: Required[str]

    search_terms: Required[Annotated[SequenceNotStr[str], PropertyInfo(alias="searchTerms")]]

    search_term_type: Required[Annotated[str, PropertyInfo(alias="searchTermType")]]
