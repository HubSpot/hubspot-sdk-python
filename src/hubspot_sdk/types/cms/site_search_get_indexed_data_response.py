# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["SiteSearchGetIndexedDataResponse", "Fields"]


class Fields(BaseModel):
    metadata_field: bool = FieldInfo(alias="metadataField")

    name: str

    value: object

    values: List[object]


class SiteSearchGetIndexedDataResponse(BaseModel):
    id: str
    """The ID of the document in HubSpot."""

    fields: Dict[str, Fields]
    """The indexed fields in HubSpot."""

    type: Literal["LANDING_PAGE", "BLOG_POST", "SITE_PAGE", "KNOWLEDGE_ARTICLE", "LISTING_PAGE"]
    """The type of document.

    Can be `SITE_PAGE`, `LANDING_PAGE`, `BLOG_POST`, `LISTING_PAGE`, or
    `KNOWLEDGE_ARTICLE`.
    """
