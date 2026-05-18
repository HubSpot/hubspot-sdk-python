# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from datetime import datetime
from typing_extensions import Literal, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["EmailGetHistogramParams"]


class EmailGetHistogramParams(TypedDict, total=False):
    email_ids: Annotated[Iterable[int], PropertyInfo(alias="emailIds")]

    end_timestamp: Annotated[Union[str, datetime], PropertyInfo(alias="endTimestamp", format="iso8601")]

    interval: Literal["DAY", "HOUR", "MINUTE", "MONTH", "QUARTER", "QUARTER_HOUR", "SECOND", "WEEK", "YEAR"]

    start_timestamp: Annotated[Union[str, datetime], PropertyInfo(alias="startTimestamp", format="iso8601")]
