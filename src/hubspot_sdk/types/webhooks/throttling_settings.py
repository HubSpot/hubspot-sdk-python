# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["ThrottlingSettings"]


class ThrottlingSettings(BaseModel):
    """Configuration details for webhook throttling."""

    max_concurrent_requests: int = FieldInfo(alias="maxConcurrentRequests")
    """
    The maximum number of concurrent HTTP requests HubSpot will attempt to make to
    your app.
    """
