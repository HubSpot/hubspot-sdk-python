# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["EmailActor"]


class EmailActor(BaseModel):
    id: str

    email: str

    type: Literal["EMAIL"]
