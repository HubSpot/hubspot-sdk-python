# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["ForeignID"]


class ForeignID(BaseModel):
    id: str
    """Unique identifier for the foreign ID."""

    name: str
    """Name of the foreign ID."""

    type: str
    """Type of the foreign ID."""
