# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["MessageGetParams"]


class MessageGetParams(TypedDict, total=False):
    thread_id: Required[Annotated[int, PropertyInfo(alias="threadId")]]

    property: str
