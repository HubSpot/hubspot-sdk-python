# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["PublicFile"]


class PublicFile(BaseModel):
    file_id: str = FieldInfo(alias="fileId")

    file_usage_type: str = FieldInfo(alias="fileUsageType")

    type: Literal["FILE"]

    name: Optional[str] = None

    url: Optional[str] = None
