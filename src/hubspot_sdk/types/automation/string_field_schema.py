# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["StringFieldSchema"]


class StringFieldSchema(BaseModel):
    type: Literal["STRING"]
    """Indicates that the type is a string, with the default value being STRING."""

    format: Optional[Literal["DATE", "DATE_TIME", "OBJECT_COORDINATE", "TIME", "URI"]] = None
    """
    Specifies the format of the string, with accepted values: DATE, DATE_TIME,
    OBJECT_COORDINATE, TIME, URI.
    """
