# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["SocialMetadataParam"]


class SocialMetadataParam(TypedDict, total=False):
    media_type: Required[
        Annotated[
            Literal[
                "ARTICLE", "AUDIO", "CAROUSEL", "DOCUMENT", "GIF", "LINK", "NONE", "PHOTO", "POLL", "STORY", "VIDEO"
            ],
            PropertyInfo(alias="mediaType"),
        ]
    ]

    id: str

    description: str

    media_title: Annotated[str, PropertyInfo(alias="mediaTitle")]

    media_url: Annotated[str, PropertyInfo(alias="mediaUrl")]

    media_url_string: Annotated[str, PropertyInfo(alias="mediaUrlString")]

    thumbnail_url: Annotated[str, PropertyInfo(alias="thumbnailUrl")]
