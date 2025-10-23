# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["MessageHeaderAttachmentParam"]


class MessageHeaderAttachmentParam(TypedDict, total=False):
    type: Required[Literal["MESSAGE_HEADER"]]

    file_id: Annotated[int, PropertyInfo(alias="fileId")]

    text: str
