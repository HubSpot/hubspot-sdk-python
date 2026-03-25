# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo

__all__ = ["PublicAdsSearchFilterParam"]


class PublicAdsSearchFilterParam(TypedDict, total=False):
    ad_network: Required[Annotated[str, PropertyInfo(alias="adNetwork")]]
    """Ad network (ADWORDS, FACEBOOK, LINKEDIN, ALL)"""

    entity_type: Required[Annotated[str, PropertyInfo(alias="entityType")]]
    """Type of ad entity (KEYWORD, ADGROUP, AD, CAMPAIGN)"""

    filter_type: Required[Annotated[Literal["ADS_SEARCH"], PropertyInfo(alias="filterType")]]
    """Type of the filter (ADS_SEARCH)"""

    operator: Required[str]
    """
    Operator to be applied (CONTAINS, IS_EQUAL_TO, ENDS_WITH, STARTS_WITH, IS_KNOWN)
    """

    search_terms: Required[Annotated[SequenceNotStr[str], PropertyInfo(alias="searchTerms")]]

    search_term_type: Required[Annotated[str, PropertyInfo(alias="searchTermType")]]
    """Search term to match an ad"""
