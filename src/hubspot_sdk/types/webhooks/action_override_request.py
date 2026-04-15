# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["ActionOverrideRequest"]


class ActionOverrideRequest(BaseModel):
    associated_object_type_ids: Optional[List[str]] = FieldInfo(alias="associatedObjectTypeIds", default=None)
    """
    An array of strings, each representing an associated object type ID relevant to
    the action override.
    """

    list_ids: Optional[List[int]] = FieldInfo(alias="listIds", default=None)
    """
    An array of integers representing list IDs that are affected by the action
    override. These IDs are in int64 format.
    """

    object_ids: Optional[List[int]] = FieldInfo(alias="objectIds", default=None)
    """
    An array of integers, each representing an object ID for which the action
    override is applicable. These IDs are in int64 format.
    """

    properties: Optional[List[str]] = None
    """
    An array of strings representing specific properties to be overridden in the
    action. Each entry in the array corresponds to a property name.
    """
