# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["EmailGetHistogramParams"]


class EmailGetHistogramParams(TypedDict, total=False):
    email_ids: Annotated[Iterable[int], PropertyInfo(alias="emailIds")]

    end_timestamp: Annotated[str, PropertyInfo(alias="endTimestamp")]

    interval: Literal["DAY", "HOUR", "MINUTE", "MONTH", "QUARTER", "QUARTER_HOUR", "SECOND", "WEEK", "YEAR"]

    start_timestamp: Annotated[str, PropertyInfo(alias="startTimestamp")]
