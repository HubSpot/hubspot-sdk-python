# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["ThrottlingSettings"]


class ThrottlingSettings(BaseModel):
    max_concurrent_requests: int = FieldInfo(alias="maxConcurrentRequests")
    """The maximum number of concurrent requests allowed. This is an integer value."""
