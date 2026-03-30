# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .size import Size
from ..._models import BaseModel

__all__ = ["Margin"]


class Margin(BaseModel):
    bottom: Size

    top: Size
