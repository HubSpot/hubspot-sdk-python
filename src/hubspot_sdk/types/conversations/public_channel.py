# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["PublicChannel"]


class PublicChannel(BaseModel):
    id: str
    """The ID of the channel."""

    name: str
    """The name of the channel."""
