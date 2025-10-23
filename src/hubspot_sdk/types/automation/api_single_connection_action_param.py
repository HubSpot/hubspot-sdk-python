# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo
from .api_connection_param import APIConnectionParam

__all__ = ["APISingleConnectionActionParam"]


class APISingleConnectionActionParam(TypedDict, total=False):
    action_id: Required[Annotated[str, PropertyInfo(alias="actionId")]]
    """The ID for this action."""

    action_type_id: Required[Annotated[str, PropertyInfo(alias="actionTypeId")]]
    """The ID of the actionType to use."""

    action_type_version: Required[Annotated[int, PropertyInfo(alias="actionTypeVersion")]]
    """The version of this actionType to use."""

    fields: Required[Dict[str, object]]
    """The fields to pass into this action.

    Different action types accept different fields.
    """

    type: Required[Literal["SINGLE_CONNECTION"]]
    """
    The type of action this is, can be: "STATIC_BRANCH", "LIST_BRANCH",
    "AB_TEST_BRANCH", "CUSTOM_CODE", "WEBHOOK", or "SINGLE_CONNECTION"
    """

    connection: APIConnectionParam
