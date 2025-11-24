# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

from ..._types import SequenceNotStr

__all__ = ["MessageListParams"]


class MessageListParams(TypedDict, total=False):
    after: str

    archived: bool

    limit: int

    property: str

    sort: SequenceNotStr[str]
