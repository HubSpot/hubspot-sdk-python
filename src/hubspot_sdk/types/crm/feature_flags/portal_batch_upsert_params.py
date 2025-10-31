# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["PortalBatchUpsertParams", "PortalState"]


class PortalBatchUpsertParams(TypedDict, total=False):
    app_id: Required[Annotated[int, PropertyInfo(alias="appId")]]

    portal_states: Required[Annotated[Iterable[PortalState], PropertyInfo(alias="portalStates")]]


class PortalState(TypedDict, total=False):
    flag_state: Required[Annotated[Literal["OFF", "ON", "ABSENT"], PropertyInfo(alias="flagState")]]

    portal_id: Required[Annotated[int, PropertyInfo(alias="portalId")]]
