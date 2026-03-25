# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo
from .endpoints_param import EndpointsParam

__all__ = ["MediaBridgeCreateOembedDomainParams"]


class MediaBridgeCreateOembedDomainParams(TypedDict, total=False):
    endpoints: Required[EndpointsParam]

    portal_id: Annotated[int, PropertyInfo(alias="portalId")]
