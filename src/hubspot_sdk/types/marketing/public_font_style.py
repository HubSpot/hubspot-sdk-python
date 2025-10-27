# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["PublicFontStyle"]


class PublicFontStyle(BaseModel):
    bold: Optional[bool] = None

    color: Optional[str] = None

    font: Optional[str] = None

    italic: Optional[bool] = None

    size: Optional[int] = None

    underline: Optional[bool] = None
