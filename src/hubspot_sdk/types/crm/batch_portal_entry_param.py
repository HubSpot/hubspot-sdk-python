# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["BatchPortalEntryParam"]


class BatchPortalEntryParam(TypedDict, total=False):
    flag_state: Required[Annotated[Literal["ABSENT", "OFF", "ON"], PropertyInfo(alias="flagState")]]

    portal_id: Required[Annotated[int, PropertyInfo(alias="portalId")]]
