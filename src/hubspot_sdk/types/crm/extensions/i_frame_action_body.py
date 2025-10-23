# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["IFrameActionBody"]


class IFrameActionBody(BaseModel):
    height: int

    property_names_included: List[str] = FieldInfo(alias="propertyNamesIncluded")

    type: Literal["IFRAME"]

    url: str

    width: int

    label: Optional[str] = None
