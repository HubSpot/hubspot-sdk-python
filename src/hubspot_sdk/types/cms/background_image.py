# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["BackgroundImage"]


class BackgroundImage(BaseModel):
    background_position: str = FieldInfo(alias="backgroundPosition")

    background_size: str = FieldInfo(alias="backgroundSize")

    image_url: str = FieldInfo(alias="imageUrl")
