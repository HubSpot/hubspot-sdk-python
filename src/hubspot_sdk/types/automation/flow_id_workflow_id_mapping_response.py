# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["FlowIDWorkflowIDMappingResponse"]


class FlowIDWorkflowIDMappingResponse(BaseModel):
    flow_id: int = FieldInfo(alias="flowId")

    workflow_id: int = FieldInfo(alias="workflowId")
