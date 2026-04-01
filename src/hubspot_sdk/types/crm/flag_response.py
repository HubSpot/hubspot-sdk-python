# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["FlagResponse"]


class FlagResponse(BaseModel):
    app_id: int = FieldInfo(alias="appId")
    """The ID of the app"""

    default_state: Literal["ABSENT", "OFF", "ON"] = FieldInfo(alias="defaultState")
    """The flag state for any portal that doesn't have an override value"""

    flag_name: str = FieldInfo(alias="flagName")
    """The name of the flag"""

    override_state: Optional[Literal["ABSENT", "OFF", "ON"]] = FieldInfo(alias="overrideState", default=None)
    """
    An optional flag value that overrides all others for this flag name and app,
    including portal-level values
    """
