# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ...._models import BaseModel

__all__ = ["CardMigrateViewsResponse"]


class CardMigrateViewsResponse(BaseModel):
    message: str
    """
    A human readable message describing the error along with remediation steps where
    appropriate
    """
