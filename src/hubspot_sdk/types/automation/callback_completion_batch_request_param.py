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

__all__ = ["CallbackCompletionBatchRequestParam", "RequestContext"]

RequestContext: TypeAlias = Union[
    WorkflowsRequestContextParam,
    AgentRequestContextParam,
    CopilotRequestContextParam,
    StandaloneRequestContextParam,
    TestRequestContextParam,
]


class CallbackCompletionBatchRequestParam(TypedDict, total=False):
    callback_id: Required[Annotated[str, PropertyInfo(alias="callbackId")]]
    """The unique identifier for the callback."""

    output_fields: Required[Annotated[Dict[str, str], PropertyInfo(alias="outputFields")]]
    """Holds the output fields for the callback completion."""

    typed_outputs: Required[Annotated[object, PropertyInfo(alias="typedOutputs")]]
    """Contains the typed outputs for the callback completion."""

    failure_reason_type: Annotated[str, PropertyInfo(alias="failureReasonType")]
    """Specifies the type of failure reason for the callback completion."""

    request_context: Annotated[RequestContext, PropertyInfo(alias="requestContext")]
    """
    Defines the context of the request, which can be one of several predefined
    types.
    """
