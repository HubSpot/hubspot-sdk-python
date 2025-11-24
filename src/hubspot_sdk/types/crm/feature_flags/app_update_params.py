# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["AppUpdateParams"]


class AppUpdateParams(TypedDict, total=False):
    app_id: Required[Annotated[int, PropertyInfo(alias="appId")]]

    default_state: Required[Annotated[Literal["ABSENT", "OFF", "ON"], PropertyInfo(alias="defaultState")]]

    override_state: Annotated[Literal["ABSENT", "OFF", "ON"], PropertyInfo(alias="overrideState")]
