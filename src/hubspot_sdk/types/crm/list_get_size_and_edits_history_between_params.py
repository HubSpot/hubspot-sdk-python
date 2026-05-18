# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["ListGetSizeAndEditsHistoryBetweenParams"]


class ListGetSizeAndEditsHistoryBetweenParams(TypedDict, total=False):
    end_date: Annotated[Union[str, datetime], PropertyInfo(alias="endDate", format="iso8601")]

    start_date: Annotated[Union[str, datetime], PropertyInfo(alias="startDate", format="iso8601")]
