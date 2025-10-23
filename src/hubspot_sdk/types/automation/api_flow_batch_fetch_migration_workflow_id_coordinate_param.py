# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["APIFlowBatchFetchMigrationWorkflowIDCoordinateParam"]


class APIFlowBatchFetchMigrationWorkflowIDCoordinateParam(TypedDict, total=False):
    flow_migration_status_for_classic_workflows: Required[
        Annotated[str, PropertyInfo(alias="flowMigrationStatusForClassicWorkflows")]
    ]
    """The workflowId from the V3 API"""

    type: Required[Literal["WORKFLOW_ID"]]
    """The type of input this is, can be FLOW_ID or WORKFLOW_ID"""
