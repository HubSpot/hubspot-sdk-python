# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["IdentificationTokenResponse"]


class IdentificationTokenResponse(BaseModel):
    """
    The identification token to be passed to the Conversations JS API to identify the visitor
    """

    token: str
