# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .flow_id_workflow_id_mapping_response import FlowIDWorkflowIDMappingResponse

__all__ = ["BatchResponseFlowIDWorkflowIDMappingResponse"]


class BatchResponseFlowIDWorkflowIDMappingResponse(BaseModel):
    completed_at: datetime = FieldInfo(alias="completedAt")

    results: List[FlowIDWorkflowIDMappingResponse]

    started_at: datetime = FieldInfo(alias="startedAt")

    status: Literal["PENDING", "PROCESSING", "CANCELED", "COMPLETE"]

    links: Optional[Dict[str, str]] = None

    requested_at: Optional[datetime] = FieldInfo(alias="requestedAt", default=None)
