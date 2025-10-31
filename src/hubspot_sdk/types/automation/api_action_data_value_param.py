# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["APIActionDataValueParam"]


class APIActionDataValueParam(TypedDict, total=False):
    action_id: Required[Annotated[str, PropertyInfo(alias="actionId")]]

    data_key: Required[Annotated[str, PropertyInfo(alias="dataKey")]]

    type: Required[Literal["FIELD_DATA"]]
