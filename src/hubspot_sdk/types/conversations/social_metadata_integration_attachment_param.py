# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo
from .social_metadata_param import SocialMetadataParam

__all__ = ["SocialMetadataIntegrationAttachmentParam"]


class SocialMetadataIntegrationAttachmentParam(TypedDict, total=False):
    social_metadata: Required[Annotated[SocialMetadataParam, PropertyInfo(alias="socialMetadata")]]

    type: Required[Literal["SOCIAL_MEDIA_METADATA"]]
