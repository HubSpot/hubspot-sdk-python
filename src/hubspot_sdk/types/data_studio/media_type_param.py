# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["MediaTypeParam"]


class MediaTypeParam(TypedDict, total=False):
    parameters: Required[Dict[str, str]]
    """
    An object containing additional parameters for the media type, where each
    key-value pair is a string.
    """

    subtype: Required[str]
    """The specific subtype of the media, represented as a string."""

    type: Required[str]
    """The primary type of the media, represented as a string."""

    wildcard_subtype: Required[Annotated[bool, PropertyInfo(alias="wildcardSubtype")]]
    """A boolean indicating whether the media subtype is a wildcard."""

    wildcard_type: Required[Annotated[bool, PropertyInfo(alias="wildcardType")]]
    """A boolean indicating whether the media type is a wildcard."""
