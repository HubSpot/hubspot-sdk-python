# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["FlagResponse"]


class FlagResponse(BaseModel):
    app_id: int = FieldInfo(alias="appId")

    default_state: Literal["ABSENT", "OFF", "ON"] = FieldInfo(alias="defaultState")

    flag_name: str = FieldInfo(alias="flagName")

    override_state: Optional[Literal["ABSENT", "OFF", "ON"]] = FieldInfo(alias="overrideState", default=None)
