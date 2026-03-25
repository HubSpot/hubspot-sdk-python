# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo
from .action_execution_index_identifier_param import ActionExecutionIndexIdentifierParam

__all__ = ["WorkflowsRequestContextParam"]


class WorkflowsRequestContextParam(TypedDict, total=False):
    source: Required[Literal["WORKFLOWS"]]

    workflow_id: Required[Annotated[int, PropertyInfo(alias="workflowId")]]

    action_execution_index_identifier: Annotated[
        ActionExecutionIndexIdentifierParam, PropertyInfo(alias="actionExecutionIndexIdentifier")
    ]

    action_id: Annotated[int, PropertyInfo(alias="actionId")]
