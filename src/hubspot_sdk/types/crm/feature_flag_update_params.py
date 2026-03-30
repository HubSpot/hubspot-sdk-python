# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["FeatureFlagUpdateParams"]


class FeatureFlagUpdateParams(TypedDict, total=False):
    app_id: Required[Annotated[int, PropertyInfo(alias="appId")]]

    flag_name: Required[Annotated[str, PropertyInfo(alias="flagName")]]

    flag_state: Required[Annotated[Literal["ABSENT", "OFF", "ON"], PropertyInfo(alias="flagState")]]
    """The state that the given flag should be in for this portal"""
