# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["PublicAdsSearchFilter"]


class PublicAdsSearchFilter(BaseModel):
    ad_network: str = FieldInfo(alias="adNetwork")
    """Ad network (ADWORDS, FACEBOOK, LINKEDIN, ALL)"""

    entity_type: str = FieldInfo(alias="entityType")
    """Type of ad entity (KEYWORD, ADGROUP, AD, CAMPAIGN)"""

    filter_type: Literal["ADS_SEARCH"] = FieldInfo(alias="filterType")
    """Type of the filter (ADS_SEARCH)"""

    operator: str
    """
    Operator to be applied (CONTAINS, IS_EQUAL_TO, ENDS_WITH, STARTS_WITH, IS_KNOWN)
    """

    search_terms: List[str] = FieldInfo(alias="searchTerms")

    search_term_type: str = FieldInfo(alias="searchTermType")
    """Search term to match an ad"""
