# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["ContactURL"]


class ContactURL(BaseModel):
    url: str

    type: Optional[Literal["HOME", "WORK"]] = None
