# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .public_in_list_filter_metadata import PublicInListFilterMetadata

__all__ = ["PublicInListFilter"]


class PublicInListFilter(BaseModel):
    filter_type: Literal["IN_LIST"] = FieldInfo(alias="filterType")

    list_id: str = FieldInfo(alias="listId")

    operator: str

    metadata: Optional[PublicInListFilterMetadata] = None
