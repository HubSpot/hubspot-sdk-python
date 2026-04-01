# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo
from .pipeline_stage_input_param import PipelineStageInputParam

__all__ = ["PipelineUpdateAllPropertiesParams"]


class PipelineUpdateAllPropertiesParams(TypedDict, total=False):
    object_type: Required[Annotated[str, PropertyInfo(alias="objectType")]]

    display_order: Required[Annotated[int, PropertyInfo(alias="displayOrder")]]
    """The order for displaying this pipeline stage.

    If two pipeline stages have a matching `displayOrder`, they will be sorted
    alphabetically by label.
    """

    label: Required[str]
    """A label used to organize pipeline stages in HubSpot's UI.

    Each pipeline stage's label must be unique within that pipeline.
    """

    stages: Required[Iterable[PipelineStageInputParam]]
    """The stages associated with the pipeline.

    They can be retrieved and updated via the pipeline stages endpoints.
    """

    validate_deal_stage_usages_before_delete: Annotated[bool, PropertyInfo(alias="validateDealStageUsagesBeforeDelete")]

    validate_references_before_delete: Annotated[bool, PropertyInfo(alias="validateReferencesBeforeDelete")]
