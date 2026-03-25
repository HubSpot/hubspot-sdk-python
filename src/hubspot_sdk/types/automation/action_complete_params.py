# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union
from typing_extensions import Required, Annotated, TypeAlias, TypedDict

from ..._utils import PropertyInfo
from .test_request_context_param import TestRequestContextParam
from .agent_request_context_param import AgentRequestContextParam
from .copilot_request_context_param import CopilotRequestContextParam
from .workflows_request_context_param import WorkflowsRequestContextParam
from .standalone_request_context_param import StandaloneRequestContextParam

__all__ = ["ActionCompleteParams", "RequestContext"]


class ActionCompleteParams(TypedDict, total=False):
    output_fields: Required[Annotated[Dict[str, str], PropertyInfo(alias="outputFields")]]

    typed_outputs: Required[Annotated[object, PropertyInfo(alias="typedOutputs")]]

    failure_reason_type: Annotated[str, PropertyInfo(alias="failureReasonType")]

    request_context: Annotated[RequestContext, PropertyInfo(alias="requestContext")]


RequestContext: TypeAlias = Union[
    WorkflowsRequestContextParam,
    AgentRequestContextParam,
    CopilotRequestContextParam,
    StandaloneRequestContextParam,
    TestRequestContextParam,
]
