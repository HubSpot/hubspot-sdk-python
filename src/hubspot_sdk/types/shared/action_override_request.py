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
    An array of integers representing list IDs that are associated with the action
    override. The integers are in int64 format.
    """

    object_ids: Optional[List[int]] = FieldInfo(alias="objectIds", default=None)
    """
    An array of integers, each representing an object ID for which the action
    override is applicable. The integers are in int64 format.
    """

    properties: Optional[List[str]] = None
    """An array of strings representing the properties to be overridden in the action.

    Each string corresponds to a property name.
    """
