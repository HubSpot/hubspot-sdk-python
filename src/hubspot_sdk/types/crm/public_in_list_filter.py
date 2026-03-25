# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .public_in_list_filter_metadata import PublicInListFilterMetadata

__all__ = ["PublicInListFilter"]


class PublicInListFilter(BaseModel):
    filter_type: Literal["IN_LIST"] = FieldInfo(alias="filterType")
    """Indicates the type of filter being applied (IN_LIST)."""

    list_id: str = FieldInfo(alias="listId")
    """The ID of the list used in the association filter."""

    operator: str
    """Specifies the operation to be performed by the filter (IN_LIST, NOT_IN_LIST)."""

    metadata: Optional[PublicInListFilterMetadata] = None
