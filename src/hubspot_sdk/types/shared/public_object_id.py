# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["PublicObjectID"]


class PublicObjectID(BaseModel):
    """Contains the Id of a Public Object"""

    id: str
    """ID of the object"""
