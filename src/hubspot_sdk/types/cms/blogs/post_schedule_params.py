# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["PostScheduleParams"]


class PostScheduleParams(TypedDict, total=False):
    id: Required[str]
    """The ID of the object to be scheduled."""

    publish_date: Required[Annotated[Union[str, datetime], PropertyInfo(alias="publishDate", format="iso8601")]]
    """The date the object should transition from scheduled to published."""
