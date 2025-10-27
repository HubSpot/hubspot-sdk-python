# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["ThreadUpdateParams"]


class ThreadUpdateParams(TypedDict, total=False):
    archived: bool
    """Whether this thread is archived. Set to false to restore the thread."""

    status: Literal["OPEN", "CLOSED"]
    """The thread's status: `OPEN` or `CLOSED`."""
