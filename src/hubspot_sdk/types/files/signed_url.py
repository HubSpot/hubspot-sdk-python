# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["SignedURL"]


class SignedURL(BaseModel):
    """Signed Url object with optional ancillary metadata of requested file"""

    expires_at: datetime = FieldInfo(alias="expiresAt")
    """Timestamp of when the URL will no longer grant access to the file."""

    extension: str
    """Extension of the requested file."""

    name: str
    """Name of the requested file."""

    size: int
    """Size in bytes of the requested file."""

    type: str
    """Type of the file. Can be IMG, DOCUMENT, AUDIO, MOVIE, or OTHER."""

    url: str
    """Signed URL with access to the specified file.

    Anyone with this URL will be able to access the file until it expires.
    """

    height: Optional[int] = None
    """For image and video files. The height of the file."""

    width: Optional[int] = None
    """For image and video files. The width of the file."""
