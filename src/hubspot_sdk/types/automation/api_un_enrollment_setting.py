# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["APIUnEnrollmentSetting"]


class APIUnEnrollmentSetting(BaseModel):
    flow_ids: List[str] = FieldInfo(alias="flowIds")

    type: Literal["ALL", "SELECTIVE"]
