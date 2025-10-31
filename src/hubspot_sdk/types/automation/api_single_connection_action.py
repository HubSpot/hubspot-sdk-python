# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .api_connection import APIConnection

__all__ = ["APISingleConnectionAction"]


class APISingleConnectionAction(BaseModel):
    action_id: str = FieldInfo(alias="actionId")

    action_type_id: str = FieldInfo(alias="actionTypeId")

    action_type_version: int = FieldInfo(alias="actionTypeVersion")

    fields: Dict[str, object]

    type: Literal["SINGLE_CONNECTION"]

    connection: Optional[APIConnection] = None
