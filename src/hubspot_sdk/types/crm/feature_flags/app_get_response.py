# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["AppGetResponse"]


class AppGetResponse(BaseModel):
    app_id: int = FieldInfo(alias="appId")

    default_state: Literal["OFF", "ON", "ABSENT"] = FieldInfo(alias="defaultState")

    flag_name: str = FieldInfo(alias="flagName")

    override_state: Optional[Literal["OFF", "ON", "ABSENT"]] = FieldInfo(alias="overrideState", default=None)
