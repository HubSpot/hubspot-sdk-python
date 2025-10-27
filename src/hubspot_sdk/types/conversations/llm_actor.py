# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["LlmActor"]


class LlmActor(BaseModel):
    id: str

    type: Literal["LLM"]

    avatar: Optional[str] = None

    name: Optional[str] = None
