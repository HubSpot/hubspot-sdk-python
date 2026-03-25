# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["ListUpdateResponse"]


class ListUpdateResponse(BaseModel):
    updated_list: Optional["PublicObjectList"] = FieldInfo(alias="updatedList", default=None)


from .public_object_list import PublicObjectList
