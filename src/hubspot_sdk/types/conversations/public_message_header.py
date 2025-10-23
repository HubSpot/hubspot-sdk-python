# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["PublicMessageHeader"]


class PublicMessageHeader(BaseModel):
    type: Literal["MESSAGE_HEADER"]

    file_id: Optional[int] = FieldInfo(alias="fileId", default=None)

    text: Optional[str] = None
