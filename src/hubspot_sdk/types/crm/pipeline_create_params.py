# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo
from .pipeline_stage_input_param import PipelineStageInputParam

__all__ = ["PipelineCreateParams"]


class PipelineCreateParams(TypedDict, total=False):
    display_order: Required[Annotated[int, PropertyInfo(alias="displayOrder")]]
    """The order for displaying this pipeline.

    If two pipelines have a matching `displayOrder`, they will be sorted
    alphabetically by label.
    """

    label: Required[str]
    """A unique label used to organize pipelines in HubSpot's UI"""

    stages: Required[Iterable[PipelineStageInputParam]]
    """Pipeline stage inputs used to create the new or replacement pipeline."""

    pipeline_id: Annotated[str, PropertyInfo(alias="pipelineId")]
