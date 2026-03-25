# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .social_metadata import SocialMetadata

__all__ = ["PublicSocialMetadataAttachment"]


class PublicSocialMetadataAttachment(BaseModel):
    social_metadata: SocialMetadata = FieldInfo(alias="socialMetadata")

    type: Literal["SOCIAL_MEDIA_METADATA"]
