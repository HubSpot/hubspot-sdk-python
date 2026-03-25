# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["PublicInListFilterMetadataParam"]


class PublicInListFilterMetadataParam(TypedDict, total=False):
    id: Required[str]
    """The identifier for the filter metadata."""

    in_list_type: Required[Annotated[str, PropertyInfo(alias="inListType")]]
    """
    Specifies the type of list for the filter (WORKFLOWS_ENROLLMENT,
    WORKFLOWS_ACTIVE, WORKFLOWS_GOAL, WORKFLOWS_COMPLETED, IMPORT, DATASET,
    DATASETS).
    """
