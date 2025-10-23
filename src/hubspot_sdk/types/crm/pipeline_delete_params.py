# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["PipelineDeleteParams"]


class PipelineDeleteParams(TypedDict, total=False):
    object_type: Required[Annotated[str, PropertyInfo(alias="objectType")]]

    validate_deal_stage_usages_before_delete: Annotated[bool, PropertyInfo(alias="validateDealStageUsagesBeforeDelete")]

    validate_references_before_delete: Annotated[bool, PropertyInfo(alias="validateReferencesBeforeDelete")]
