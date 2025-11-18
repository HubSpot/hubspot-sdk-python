# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["ContactMergeParams"]


class ContactMergeParams(TypedDict, total=False):
    object_id_to_merge: Required[Annotated[str, PropertyInfo(alias="objectIdToMerge")]]
    """
    The unique identifier of the CRM object that will be merged into the primary
    object.
    """

    primary_object_id: Required[Annotated[str, PropertyInfo(alias="primaryObjectId")]]
    """The unique identifier of the CRM object that will remain after the merge."""
