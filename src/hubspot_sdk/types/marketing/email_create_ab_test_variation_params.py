# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["EmailCreateAbTestVariationParams"]


class EmailCreateAbTestVariationParams(TypedDict, total=False):
    content_id: Required[Annotated[str, PropertyInfo(alias="contentId")]]
    """ID of the email to test."""

    variation_name: Required[Annotated[str, PropertyInfo(alias="variationName")]]
    """Name of the variation to be created."""
