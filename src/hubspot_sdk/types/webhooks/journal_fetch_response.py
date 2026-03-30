# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["JournalFetchResponse"]


class JournalFetchResponse(BaseModel):
    current_offset: str = FieldInfo(alias="currentOffset")

    expires_at: datetime = FieldInfo(alias="expiresAt")

    url: str
