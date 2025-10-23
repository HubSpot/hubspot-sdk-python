# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from typing_extensions import Required, TypeAlias, TypedDict

from .api_flow_batch_fetch_migration_flow_id_coordinate_param import APIFlowBatchFetchMigrationFlowIDCoordinateParam
from .api_flow_batch_fetch_migration_workflow_id_coordinate_param import (
    APIFlowBatchFetchMigrationWorkflowIDCoordinateParam,
)

__all__ = ["WorkflowBatchGetIDMappingsParams", "Input"]


class WorkflowBatchGetIDMappingsParams(TypedDict, total=False):
    inputs: Required[Iterable[Input]]


Input: TypeAlias = Union[
    APIFlowBatchFetchMigrationFlowIDCoordinateParam, APIFlowBatchFetchMigrationWorkflowIDCoordinateParam
]
