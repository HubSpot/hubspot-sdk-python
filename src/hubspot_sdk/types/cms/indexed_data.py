# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict
from typing_extensions import Literal

from ..._models import BaseModel
from .indexed_field import IndexedField

__all__ = ["IndexedData"]


class IndexedData(BaseModel):
    id: str
    """The ID of the document in HubSpot."""

    fields: Dict[str, IndexedField]
    """The indexed fields in HubSpot."""

    type: Literal["BLOG_POST", "KNOWLEDGE_ARTICLE", "LANDING_PAGE", "LISTING_PAGE", "SITE_PAGE", "STRUCTURED_CONTENT"]
    """The type of document.

    Can be `SITE_PAGE`, `LANDING_PAGE`, `BLOG_POST`, `LISTING_PAGE`, or
    `KNOWLEDGE_ARTICLE`.
    """
