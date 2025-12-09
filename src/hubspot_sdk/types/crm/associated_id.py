# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["AssociatedID"]


class AssociatedID(BaseModel):
    """Contains the id and type of an association"""

    id: str
    """The ID for the association type."""

    type: str
    """The type of association."""
