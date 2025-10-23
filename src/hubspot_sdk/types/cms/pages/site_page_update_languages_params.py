# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["SitePageUpdateLanguagesParams"]


class SitePageUpdateLanguagesParams(TypedDict, total=False):
    languages: Required[Dict[str, str]]
    """
    Map of object IDs to associated languages of object in the multi-language group.
    """

    primary_id: Required[Annotated[str, PropertyInfo(alias="primaryId")]]
    """ID of the primary object in the multi-language group."""
