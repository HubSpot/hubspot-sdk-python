# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .video_object import VideoObject

__all__ = ["MediaBridgeObject"]


class MediaBridgeObject(BaseModel):
    id: str

    created_at: datetime = FieldInfo(alias="createdAt")

    media_type: Literal["AUDIO", "DOCUMENT", "IMAGE", "OTHER", "VIDEO"] = FieldInfo(alias="mediaType")

    title: str

    updated_at: datetime = FieldInfo(alias="updatedAt")

    details_page_link: Optional[str] = FieldInfo(alias="detailsPageLink", default=None)

    duration: Optional[int] = None

    external_id: Optional[str] = FieldInfo(alias="externalId", default=None)

    file_url: Optional[str] = FieldInfo(alias="fileUrl", default=None)

    oembed_url: Optional[str] = FieldInfo(alias="oembedUrl", default=None)

    poster_url: Optional[str] = FieldInfo(alias="posterUrl", default=None)

    thumbnail_url: Optional[str] = FieldInfo(alias="thumbnailUrl", default=None)

    video: Optional[VideoObject] = None
