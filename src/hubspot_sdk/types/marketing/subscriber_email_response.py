# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["SubscriberEmailResponse"]


class SubscriberEmailResponse(BaseModel):
    email: str
    """The email of the contact"""

    vid: int
    """The internal ID of the contact"""
