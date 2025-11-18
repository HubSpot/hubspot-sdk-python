# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["PipelineUpdateParams"]


class PipelineUpdateParams(TypedDict, total=False):
    object_type: Required[Annotated[str, PropertyInfo(alias="objectType")]]

    validate_deal_stage_usages_before_delete: Annotated[bool, PropertyInfo(alias="validateDealStageUsagesBeforeDelete")]
    """Indicates whether to validate deal stage usages before deleting the pipeline."""

    validate_references_before_delete: Annotated[bool, PropertyInfo(alias="validateReferencesBeforeDelete")]
    """Indicates whether to validate references before deleting the pipeline."""

    archived: bool
    """Whether the pipeline is archived.

    This property should only be provided when restoring an archived pipeline. If
    it's provided in any other call, the request will fail and a `400 Bad Request`
    will be returned.
    """

    display_order: Annotated[int, PropertyInfo(alias="displayOrder")]
    """The order for displaying this pipeline.

    If two pipelines have a matching `displayOrder`, they will be sorted
    alphabetically by label.
    """

    label: str
    """A unique label used to organize pipelines in HubSpot's UI"""
