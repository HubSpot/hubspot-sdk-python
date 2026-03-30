# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["PortalFlagStateResponse"]


class PortalFlagStateResponse(BaseModel):
    app_id: int = FieldInfo(alias="appId")
    """The ID of the app"""

    flag_name: str = FieldInfo(alias="flagName")
    """The name of the flag"""

    flag_state: Literal["ABSENT", "OFF", "ON"] = FieldInfo(alias="flagState")
    """The state of the flag for this portal"""

    portal_id: int = FieldInfo(alias="portalId")
    """The ID of the portal"""
