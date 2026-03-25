# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["SocialMetadata"]


class SocialMetadata(BaseModel):
    media_type: Literal[
        "ARTICLE", "AUDIO", "CAROUSEL", "DOCUMENT", "GIF", "LINK", "NONE", "PHOTO", "POLL", "STORY", "VIDEO"
    ] = FieldInfo(alias="mediaType")

    id: Optional[str] = None

    description: Optional[str] = None

    media_title: Optional[str] = FieldInfo(alias="mediaTitle", default=None)

    media_url: Optional[str] = FieldInfo(alias="mediaUrl", default=None)

    media_url_string: Optional[str] = FieldInfo(alias="mediaUrlString", default=None)

    thumbnail_url: Optional[str] = FieldInfo(alias="thumbnailUrl", default=None)
