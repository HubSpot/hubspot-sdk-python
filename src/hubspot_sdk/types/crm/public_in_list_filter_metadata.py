# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["PublicInListFilterMetadata"]


class PublicInListFilterMetadata(BaseModel):
    id: str
    """The identifier for the filter metadata."""

    in_list_type: str = FieldInfo(alias="inListType")
    """
    Specifies the type of list for the filter (WORKFLOWS_ENROLLMENT,
    WORKFLOWS_ACTIVE, WORKFLOWS_GOAL, WORKFLOWS_COMPLETED, IMPORT, DATASET,
    DATASETS).
    """
