# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, Annotated, TypedDict

from ...._utils import PropertyInfo
from ..batch_portal_entry_param import BatchPortalEntryParam

__all__ = ["PortalBatchUpsertParams"]


class PortalBatchUpsertParams(TypedDict, total=False):
    app_id: Required[Annotated[int, PropertyInfo(alias="appId")]]

    portal_states: Required[Annotated[Iterable[BatchPortalEntryParam], PropertyInfo(alias="portalStates")]]
