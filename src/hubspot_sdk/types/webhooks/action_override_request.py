# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["ActionOverrideRequest"]


class ActionOverrideRequest(BaseModel):
    associated_object_type_ids: Optional[List[str]] = FieldInfo(alias="associatedObjectTypeIds", default=None)

    list_ids: Optional[List[int]] = FieldInfo(alias="listIds", default=None)

    object_ids: Optional[List[int]] = FieldInfo(alias="objectIds", default=None)

    properties: Optional[List[str]] = None
