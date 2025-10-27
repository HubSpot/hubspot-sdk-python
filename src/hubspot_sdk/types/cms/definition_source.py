# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["DefinitionSource"]


class DefinitionSource(BaseModel):
    type: str

    name: Optional[str] = None
