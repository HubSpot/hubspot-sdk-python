# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .pipeline import Pipeline
from ..._models import BaseModel

__all__ = ["CollectionResponsePipelineNoPaging"]


class CollectionResponsePipelineNoPaging(BaseModel):
    results: List[Pipeline]
