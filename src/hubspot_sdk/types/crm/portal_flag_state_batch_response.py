# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .portal_flag_state_response import PortalFlagStateResponse

__all__ = ["PortalFlagStateBatchResponse"]


class PortalFlagStateBatchResponse(BaseModel):
    portal_flag_states: List[PortalFlagStateResponse] = FieldInfo(alias="portalFlagStates")
