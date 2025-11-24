# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["VisitorActor"]


class VisitorActor(BaseModel):
    id: str

    type: Literal["VISITOR"]

    avatar: Optional[str] = None

    email: Optional[str] = None

    name: Optional[str] = None
