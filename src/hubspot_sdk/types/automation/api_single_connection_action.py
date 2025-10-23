# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .api_connection import APIConnection

__all__ = ["APISingleConnectionAction"]


class APISingleConnectionAction(BaseModel):
    action_id: str = FieldInfo(alias="actionId")
    """The ID for this action."""

    action_type_id: str = FieldInfo(alias="actionTypeId")
    """The ID of the actionType to use."""

    action_type_version: int = FieldInfo(alias="actionTypeVersion")
    """The version of this actionType to use."""

    fields: Dict[str, object]
    """The fields to pass into this action.

    Different action types accept different fields.
    """

    type: Literal["SINGLE_CONNECTION"]
    """
    The type of action this is, can be: "STATIC_BRANCH", "LIST_BRANCH",
    "AB_TEST_BRANCH", "CUSTOM_CODE", "WEBHOOK", or "SINGLE_CONNECTION"
    """

    connection: Optional[APIConnection] = None
