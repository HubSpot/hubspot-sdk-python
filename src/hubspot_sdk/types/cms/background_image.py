# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["BackgroundImage"]


class BackgroundImage(BaseModel):
    background_position: str = FieldInfo(alias="backgroundPosition")
    """Defines the position of the background image."""

    background_size: str = FieldInfo(alias="backgroundSize")
    """Specifies the size of the background image."""

    image_url: str = FieldInfo(alias="imageUrl")
    """The URL of the background image."""
