# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["PublicAdsSearchFilter"]


class PublicAdsSearchFilter(BaseModel):
    ad_network: str = FieldInfo(alias="adNetwork")

    entity_type: str = FieldInfo(alias="entityType")

    filter_type: Literal["ADS_SEARCH"] = FieldInfo(alias="filterType")

    operator: str

    search_terms: List[str] = FieldInfo(alias="searchTerms")

    search_term_type: str = FieldInfo(alias="searchTermType")
