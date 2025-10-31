# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ...._types import SequenceNotStr
from ...._utils import PropertyInfo

__all__ = ["IntegratorSettingCreateOembedDomainParams", "Endpoints"]


class IntegratorSettingCreateOembedDomainParams(TypedDict, total=False):
    endpoints: Required[Endpoints]

    portal_id: Annotated[int, PropertyInfo(alias="portalId")]


class Endpoints(TypedDict, total=False):
    discovery: Required[bool]

    schemes: Required[SequenceNotStr[str]]

    url: Required[str]
