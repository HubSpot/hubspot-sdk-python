# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from datetime import datetime

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .list_size_data_point import ListSizeDataPoint

__all__ = ["ListSizeAndEditHistoryResponse"]


class ListSizeAndEditHistoryResponse(BaseModel):
    edit_history: List[datetime] = FieldInfo(alias="editHistory")

    size_history: List[ListSizeDataPoint] = FieldInfo(alias="sizeHistory")
