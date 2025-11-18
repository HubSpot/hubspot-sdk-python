# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["IntegratorSettingDeleteOembedDomainParams"]


class IntegratorSettingDeleteOembedDomainParams(TypedDict, total=False):
    id: int
    """The ID of the oEmbed to delete."""

    domain_portal_id: Annotated[int, PropertyInfo(alias="domainPortalId")]
    """Filter response by Hub ID."""
