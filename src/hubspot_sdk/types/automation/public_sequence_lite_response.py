# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["PublicSequenceLiteResponse"]


class PublicSequenceLiteResponse(BaseModel):
    id: str
    """The unique identifier of the sequence."""

    created_at: datetime = FieldInfo(alias="createdAt")
    """The date and time when the sequence was created."""

    name: str
    """The name of the sequence."""

    updated_at: datetime = FieldInfo(alias="updatedAt")
    """The date and time when the sequence was last updated."""

    user_id: str = FieldInfo(alias="userId")
    """The ID of the user associated with the sequence."""

    folder_id: Optional[str] = FieldInfo(alias="folderId", default=None)
    """The ID of the folder containing the sequence."""
