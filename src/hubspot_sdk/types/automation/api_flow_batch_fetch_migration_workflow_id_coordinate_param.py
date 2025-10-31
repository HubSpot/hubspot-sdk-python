# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["APIFlowBatchFetchMigrationWorkflowIDCoordinateParam"]


class APIFlowBatchFetchMigrationWorkflowIDCoordinateParam(TypedDict, total=False):
    flow_migration_status_for_classic_workflows: Required[
        Annotated[str, PropertyInfo(alias="flowMigrationStatusForClassicWorkflows")]
    ]

    type: Required[Literal["WORKFLOW_ID"]]
