# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["PortalFlagStateResponse"]


class PortalFlagStateResponse(BaseModel):
    app_id: int = FieldInfo(alias="appId")

    flag_name: str = FieldInfo(alias="flagName")

    flag_state: Literal["ABSENT", "OFF", "ON"] = FieldInfo(alias="flagState")

    portal_id: int = FieldInfo(alias="portalId")
