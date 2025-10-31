# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["PortalUpdateResponse"]


class PortalUpdateResponse(BaseModel):
    app_id: int = FieldInfo(alias="appId")

    flag_name: str = FieldInfo(alias="flagName")

    flag_state: Literal["OFF", "ON", "ABSENT"] = FieldInfo(alias="flagState")

    portal_id: int = FieldInfo(alias="portalId")
