# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["BackgroundImageParam"]


class BackgroundImageParam(TypedDict, total=False):
    background_position: Required[Annotated[str, PropertyInfo(alias="backgroundPosition")]]
    """Defines the position of the background image."""

    background_size: Required[Annotated[str, PropertyInfo(alias="backgroundSize")]]
    """Specifies the size of the background image."""

    image_url: Required[Annotated[str, PropertyInfo(alias="imageUrl")]]
    """The URL of the background image."""
