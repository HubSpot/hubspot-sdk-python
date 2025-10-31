# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["FileAttachmentParam"]


class FileAttachmentParam(TypedDict, total=False):
    file_id: Required[Annotated[str, PropertyInfo(alias="fileId")]]

    type: Required[Literal["FILE"]]

    file_usage_type: Annotated[str, PropertyInfo(alias="fileUsageType")]
