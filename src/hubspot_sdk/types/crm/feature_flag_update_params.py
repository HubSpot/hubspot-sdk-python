# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["FeatureFlagUpdateParams"]


class FeatureFlagUpdateParams(TypedDict, total=False):
    app_id: Required[Annotated[int, PropertyInfo(alias="appId")]]

    default_state: Required[Annotated[Literal["ABSENT", "OFF", "ON"], PropertyInfo(alias="defaultState")]]
    """
    The state that the flag should have if there are no overrides for a particular
    portal
    """

    override_state: Annotated[Literal["ABSENT", "OFF", "ON"], PropertyInfo(alias="overrideState")]
    """A flag value that supercedes all other overrides, including portal-level values.

    Mostly used for things like emergency overrides
    """
