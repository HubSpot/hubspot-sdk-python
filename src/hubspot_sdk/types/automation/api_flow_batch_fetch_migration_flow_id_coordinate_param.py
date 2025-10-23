# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["APIFlowBatchFetchMigrationFlowIDCoordinateParam"]


class APIFlowBatchFetchMigrationFlowIDCoordinateParam(TypedDict, total=False):
    flow_migration_statuses: Required[Annotated[str, PropertyInfo(alias="flowMigrationStatuses")]]
    """The flowId from the V4 API"""

    type: Required[Literal["FLOW_ID"]]
    """The type of input this is, can be FLOW_ID or WORKFLOW_ID"""
