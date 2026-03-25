# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["PublicTeam"]


class PublicTeam(BaseModel):
    id: str

    name: str

    primary: bool
