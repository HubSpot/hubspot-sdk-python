# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, TypedDict

__all__ = ["ThreadGetParams"]


class ThreadGetParams(TypedDict, total=False):
    archived: bool
    """Whether to return only results that have been archived. Default is false."""

    association: List[Literal["TICKET"]]
    """You can specify an association type here of `TICKET`.

    If this is set the response will included a thread associations object and
    associated ticket id if present. If there are no associations to a ticket with
    this conversation, then the thread associations object will not be present on
    the response.
    """

    property: str
    """A specific property to include in the thread response."""
