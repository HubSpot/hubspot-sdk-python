# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["CustomMergeParams"]


class CustomMergeParams(TypedDict, total=False):
    object_id_to_merge: Required[Annotated[str, PropertyInfo(alias="objectIdToMerge")]]
    """
    The object ID of the record that the merge will not set as the current value
    after the merge.
    """

    primary_object_id: Required[Annotated[str, PropertyInfo(alias="primaryObjectId")]]
    """
    The object ID of the record that the merge will generally set as the current
    value after the merge.
    """
