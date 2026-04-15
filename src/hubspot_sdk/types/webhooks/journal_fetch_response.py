# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["JournalFetchResponse"]


class JournalFetchResponse(BaseModel):
    current_offset: str = FieldInfo(alias="currentOffset")
    """
    A UUID string indicating the current offset in the journal data, used for
    pagination.
    """

    expires_at: datetime = FieldInfo(alias="expiresAt")
    """The date and time when the URL will expire, in ISO 8601 format."""

    url: str
    """A string representing the URL where the fetched journal data can be accessed."""
