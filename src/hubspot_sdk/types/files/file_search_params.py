# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from datetime import datetime
from typing_extensions import Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo

__all__ = ["FileSearchParams"]


class FileSearchParams(TypedDict, total=False):
    after: str
    """
    The paging cursor token of the last successfully read resource will be returned
    as the `paging.next.after` JSON property of a paged response containing more
    results.
    """

    allows_anonymous_access: Annotated[bool, PropertyInfo(alias="allowsAnonymousAccess")]

    before: str

    created_at: Annotated[Union[str, datetime], PropertyInfo(alias="createdAt", format="iso8601")]

    created_at_gte: Annotated[Union[str, datetime], PropertyInfo(alias="createdAtGte", format="iso8601")]

    created_at_lte: Annotated[Union[str, datetime], PropertyInfo(alias="createdAtLte", format="iso8601")]

    encoding: str

    expires_at: Annotated[Union[str, datetime], PropertyInfo(alias="expiresAt", format="iso8601")]

    expires_at_gte: Annotated[Union[str, datetime], PropertyInfo(alias="expiresAtGte", format="iso8601")]

    expires_at_lte: Annotated[Union[str, datetime], PropertyInfo(alias="expiresAtLte", format="iso8601")]

    extension: str

    file_md5: Annotated[str, PropertyInfo(alias="fileMd5")]

    height: int

    height_gte: Annotated[int, PropertyInfo(alias="heightGte")]

    height_lte: Annotated[int, PropertyInfo(alias="heightLte")]

    id_gte: Annotated[int, PropertyInfo(alias="idGte")]

    id_lte: Annotated[int, PropertyInfo(alias="idLte")]

    ids: Iterable[int]

    is_usable_in_content: Annotated[bool, PropertyInfo(alias="isUsableInContent")]

    limit: int
    """The maximum number of results to display per page."""

    name: str

    parent_folder_ids: Annotated[Iterable[int], PropertyInfo(alias="parentFolderIds")]

    path: str

    properties: SequenceNotStr[str]

    size: int

    size_gte: Annotated[int, PropertyInfo(alias="sizeGte")]

    size_lte: Annotated[int, PropertyInfo(alias="sizeLte")]

    sort: SequenceNotStr[str]

    type: str

    updated_at: Annotated[Union[str, datetime], PropertyInfo(alias="updatedAt", format="iso8601")]

    updated_at_gte: Annotated[Union[str, datetime], PropertyInfo(alias="updatedAtGte", format="iso8601")]

    updated_at_lte: Annotated[Union[str, datetime], PropertyInfo(alias="updatedAtLte", format="iso8601")]

    url: str

    width: int

    width_gte: Annotated[int, PropertyInfo(alias="widthGte")]

    width_lte: Annotated[int, PropertyInfo(alias="widthLte")]
