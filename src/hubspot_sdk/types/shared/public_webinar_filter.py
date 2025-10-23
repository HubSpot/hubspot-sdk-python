# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["PublicWebinarFilter"]


class PublicWebinarFilter(BaseModel):
    filter_type: Literal["WEBINAR"] = FieldInfo(alias="filterType")

    operator: str

    webinar_id: Optional[str] = FieldInfo(alias="webinarId", default=None)
