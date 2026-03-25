# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["ContactEmail"]


class ContactEmail(BaseModel):
    email: str

    type: Optional[Literal["HOME", "WORK"]] = None
