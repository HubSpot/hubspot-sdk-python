# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["FlagsForAppResponse"]


class FlagsForAppResponse(BaseModel):
    flags_for_app: List[str] = FieldInfo(alias="flagsForApp")
