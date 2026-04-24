# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["JournalFetchResponse"]


class JournalFetchResponse(BaseModel):
    current_offset: str = FieldInfo(alias="currentOffset")
    """
    The unique identifier for the current offset of the journal entry, formatted as
    a UUID.
    """

    expires_at: datetime = FieldInfo(alias="expiresAt")
    """The date and time when the URL will expire, in ISO 8601 format."""

    url: str
    """The URL where the journal entry can be accessed. It is a string."""
