# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .size import Size
from ..._models import BaseModel

__all__ = ["Padding"]


class Padding(BaseModel):
    bottom: Size

    left: Size

    right: Size

    top: Size
