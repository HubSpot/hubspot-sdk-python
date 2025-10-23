# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel
from .pipeline_stage import PipelineStage

__all__ = ["CollectionResponsePipelineStageNoPaging"]


class CollectionResponsePipelineStageNoPaging(BaseModel):
    results: List[PipelineStage]
