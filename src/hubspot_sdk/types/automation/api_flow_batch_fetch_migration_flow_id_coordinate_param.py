# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["APIFlowBatchFetchMigrationFlowIDCoordinateParam"]


class APIFlowBatchFetchMigrationFlowIDCoordinateParam(TypedDict, total=False):
    flow_migration_statuses: Required[Annotated[str, PropertyInfo(alias="flowMigrationStatuses")]]

    type: Required[Literal["FLOW_ID"]]
