# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo
from .api_connection_param import APIConnectionParam

__all__ = ["APISingleConnectionActionParam"]


class APISingleConnectionActionParam(TypedDict, total=False):
    action_id: Required[Annotated[str, PropertyInfo(alias="actionId")]]

    action_type_id: Required[Annotated[str, PropertyInfo(alias="actionTypeId")]]

    action_type_version: Required[Annotated[int, PropertyInfo(alias="actionTypeVersion")]]

    fields: Required[Dict[str, object]]

    type: Required[Literal["SINGLE_CONNECTION"]]

    connection: APIConnectionParam
