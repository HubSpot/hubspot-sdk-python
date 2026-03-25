# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["VideoObject"]


class VideoObject(BaseModel):
    id: int

    deeplink_url: str = FieldInfo(alias="deeplinkUrl")

    file_id: int = FieldInfo(alias="fileId")
