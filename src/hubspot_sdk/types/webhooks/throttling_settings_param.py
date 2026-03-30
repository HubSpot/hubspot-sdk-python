# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["ThrottlingSettingsParam"]


class ThrottlingSettingsParam(TypedDict, total=False):
    max_concurrent_requests: Required[Annotated[int, PropertyInfo(alias="maxConcurrentRequests")]]
    """
    The maximum number of HTTP requests HubSpot will attempt to make to your app in
    a given time frame determined by `period`.
    """
