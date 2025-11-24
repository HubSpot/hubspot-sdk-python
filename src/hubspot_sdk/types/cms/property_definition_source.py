# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["PropertyDefinitionSource"]


class PropertyDefinitionSource(BaseModel):
    type: Literal["GLOBAL", "HAVEN_BRANCH", "OBJECT_TYPE", "PORTAL"]

    name: Optional[str] = None
