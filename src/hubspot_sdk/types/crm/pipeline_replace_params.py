# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["PipelineReplaceParams"]


class PipelineReplaceParams(TypedDict, total=False):
    object_type: Required[Annotated[str, PropertyInfo(alias="objectType")]]

    pipeline_id: Required[Annotated[str, PropertyInfo(alias="pipelineId")]]

    display_order: Required[Annotated[int, PropertyInfo(alias="displayOrder")]]

    label: Required[str]

    metadata: Required[Dict[str, str]]
