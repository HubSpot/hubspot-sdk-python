# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["IFrameActionBody"]


class IFrameActionBody(BaseModel):
    height: int
    """The height of the iframe in pixels."""

    property_names_included: List[str] = FieldInfo(alias="propertyNamesIncluded")
    """A list of property names that will be included on the url of the iframe."""

    type: Literal["IFRAME"]
    """The type of status."""

    url: str
    """The URL endpoint that will be loaded in the iframe when triggered."""

    width: int
    """The width of the iframe in pixels."""

    label: Optional[str] = None
    """The label for this property as you'd like it displayed to users."""
