# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["AbTestCreateRequestVNext"]


class AbTestCreateRequestVNext(BaseModel):
    """Request body object for creating A/B tests."""

    content_id: str = FieldInfo(alias="contentId")
    """ID of the object to test."""

    variation_name: str = FieldInfo(alias="variationName")
    """Name of A/B test variation."""
