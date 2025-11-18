# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["ThreadUpdateParams"]


class ThreadUpdateParams(TypedDict, total=False):
    query_archived: Annotated[bool, PropertyInfo(alias="archived")]
    """Whether the thread to update is archived.

    Default is false. A thread's status property can not be updated if the thread is
    archived.
    """

    body_archived: Annotated[bool, PropertyInfo(alias="archived")]
    """Whether this thread is archived. Set to false to restore the thread."""

    status: Literal["OPEN", "CLOSED"]
    """The thread's status: `OPEN` or `CLOSED`."""
