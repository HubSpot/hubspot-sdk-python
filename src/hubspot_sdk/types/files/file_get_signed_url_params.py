# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["FileGetSignedURLParams"]


class FileGetSignedURLParams(TypedDict, total=False):
    expiration_seconds: Annotated[int, PropertyInfo(alias="expirationSeconds")]

    size: Literal["icon", "medium", "preview", "thumb"]

    upscale: bool
