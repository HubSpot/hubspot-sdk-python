# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["MediaBridgeDeleteOembedDomainParams"]


class MediaBridgeDeleteOembedDomainParams(TypedDict, total=False):
    id: int

    domain_portal_id: Annotated[int, PropertyInfo(alias="domainPortalId")]
