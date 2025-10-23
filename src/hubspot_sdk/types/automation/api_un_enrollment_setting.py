# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["APIUnEnrollmentSetting"]


class APIUnEnrollmentSetting(BaseModel):
    flow_ids: List[str] = FieldInfo(alias="flowIds")
    """The IDs of the flows to unenroll an object in if it's enrolled in this flow."""

    type: Literal["ALL", "SELECTIVE"]
    """The type of unenrollment to perform:

    "ALL" - unenroll the object from all other flows

    "SELECTIVE" - only unenroll the object from the flows specified in `flowIds`
    """
