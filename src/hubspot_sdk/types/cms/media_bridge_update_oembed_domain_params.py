# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo
from .endpoints_param import EndpointsParam

__all__ = ["MediaBridgeUpdateOembedDomainParams"]


class MediaBridgeUpdateOembedDomainParams(TypedDict, total=False):
    app_id: Required[Annotated[int, PropertyInfo(alias="appId")]]

    endpoints: Required[EndpointsParam]

    portal_id: Annotated[int, PropertyInfo(alias="portalId")]
