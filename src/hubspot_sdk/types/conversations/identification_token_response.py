# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["IdentificationTokenResponse"]


class IdentificationTokenResponse(BaseModel):
    token: str
    """
    An identification token that allows the visitor to be treated as a known
    contact.
    """
