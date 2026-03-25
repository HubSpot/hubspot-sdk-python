# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ....._models import BaseModel

__all__ = ["Speaker"]


class Speaker(BaseModel):
    id: str

    name: str

    email: Optional[str] = None
