# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["ABTestCreateSitePageVariationParams"]


class ABTestCreateSitePageVariationParams(TypedDict, total=False):
    content_id: Required[Annotated[str, PropertyInfo(alias="contentId")]]
    """ID of the object to test."""

    variation_name: Required[Annotated[str, PropertyInfo(alias="variationName")]]
    """Name of A/B test variation."""
