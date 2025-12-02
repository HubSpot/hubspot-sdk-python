# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["FileOperationGetSignedURLParams"]


class FileOperationGetSignedURLParams(TypedDict, total=False):
    expiration_seconds: Annotated[int, PropertyInfo(alias="expirationSeconds")]
    """How long in seconds the link will provide access to the file."""

    size: Literal["icon", "medium", "preview", "thumb"]
    """For image files.

    This will resize the image to the desired size before sharing. Does not affect
    the original file, just the file served by this signed URL.
    """

    upscale: bool
    """If size is provided, this will upscale the image to fit the size dimensions."""
