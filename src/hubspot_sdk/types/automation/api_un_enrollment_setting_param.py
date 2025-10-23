# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo

__all__ = ["APIUnEnrollmentSettingParam"]


class APIUnEnrollmentSettingParam(TypedDict, total=False):
    flow_ids: Required[Annotated[SequenceNotStr[str], PropertyInfo(alias="flowIds")]]
    """The IDs of the flows to unenroll an object in if it's enrolled in this flow."""

    type: Required[Literal["ALL", "SELECTIVE"]]
    """The type of unenrollment to perform:

    "ALL" - unenroll the object from all other flows

    "SELECTIVE" - only unenroll the object from the flows specified in `flowIds`
    """
