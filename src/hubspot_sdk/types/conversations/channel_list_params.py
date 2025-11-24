# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo

__all__ = ["ChannelListParams"]


class ChannelListParams(TypedDict, total=False):
    after: str

    default_page_length: Annotated[int, PropertyInfo(alias="defaultPageLength")]

    limit: int

    sort: SequenceNotStr[str]
