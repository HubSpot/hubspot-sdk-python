# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["UpdateVideoObjectRequestParam"]


class UpdateVideoObjectRequestParam(TypedDict, total=False):
    media_type: Required[Annotated[Literal["VIDEO"], PropertyInfo(alias="mediaType")]]

    bearer_token: Annotated[str, PropertyInfo(alias="bearerToken")]

    details_page_link: Annotated[str, PropertyInfo(alias="detailsPageLink")]

    duration: int

    external_id: Annotated[str, PropertyInfo(alias="externalId")]

    file_url: Annotated[str, PropertyInfo(alias="fileUrl")]

    oembed_url: Annotated[str, PropertyInfo(alias="oembedUrl")]

    poster_url: Annotated[str, PropertyInfo(alias="posterUrl")]

    thumbnail_url: Annotated[str, PropertyInfo(alias="thumbnailUrl")]

    title: str

    transcript_url: Annotated[str, PropertyInfo(alias="transcriptUrl")]
