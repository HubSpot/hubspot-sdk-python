# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["ThreadUpdateParams"]


class ThreadUpdateParams(TypedDict, total=False):
    query_archived: Annotated[bool, PropertyInfo(alias="archived")]

    body_archived: Annotated[bool, PropertyInfo(alias="archived")]

    status: Literal["CLOSED", "OPEN"]
