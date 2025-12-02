# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from datetime import datetime
from typing_extensions import Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo

__all__ = ["FileOperationSearchParams"]


class FileOperationSearchParams(TypedDict, total=False):
    after: str
    """Offset search results by this value.

    The default offset is 0 and the maximum offset of items for a given search is
    10,000. Narrow your search down if you are reaching this limit.
    """

    allows_anonymous_access: Annotated[bool, PropertyInfo(alias="allowsAnonymousAccess")]
    """Search files by access.

    If `true`, will show only public files. If `false`, will show only private
    files.
    """

    before: str

    created_at: Annotated[Union[str, datetime], PropertyInfo(alias="createdAt", format="iso8601")]
    """Search files by time of creation."""

    created_at_gte: Annotated[Union[str, datetime], PropertyInfo(alias="createdAtGte", format="iso8601")]
    """Search files by greater than or equal to time of creation.

    Can be used with `createdAtLte` to create a range.
    """

    created_at_lte: Annotated[Union[str, datetime], PropertyInfo(alias="createdAtLte", format="iso8601")]
    """Search files by less than or equal to time of creation.

    Can be used with `createdAtGte` to create a range.
    """

    encoding: str
    """Search files by specified encoding."""

    expires_at: Annotated[Union[str, datetime], PropertyInfo(alias="expiresAt", format="iso8601")]
    """Search files by exact expires time. Time must be epoch time in milliseconds."""

    expires_at_gte: Annotated[Union[str, datetime], PropertyInfo(alias="expiresAtGte", format="iso8601")]
    """Search files by greater than or equal to expires time.

    Can be used with `expiresAtLte` to create a range.
    """

    expires_at_lte: Annotated[Union[str, datetime], PropertyInfo(alias="expiresAtLte", format="iso8601")]
    """Search files by less than or equal to expires time.

    Can be used with `expiresAtGte` to create a range.
    """

    extension: str
    """Search files by given extension."""

    file_md5: Annotated[str, PropertyInfo(alias="fileMd5")]
    """Search files by a specific md5 hash."""

    height: int
    """Search files by height of image or video."""

    height_gte: Annotated[int, PropertyInfo(alias="heightGte")]
    """Search files by greater than or equal to height of image or video.

    Can be used with `heightLte` to create a range.
    """

    height_lte: Annotated[int, PropertyInfo(alias="heightLte")]
    """Search files by less than or equal to height of image or video.

    Can be used with `heightGte` to create a range.
    """

    id_gte: Annotated[int, PropertyInfo(alias="idGte")]

    id_lte: Annotated[int, PropertyInfo(alias="idLte")]

    ids: Iterable[int]
    """Search by a list of file IDs."""

    is_usable_in_content: Annotated[bool, PropertyInfo(alias="isUsableInContent")]
    """If `true`, shows files that have been marked to be used in new content.

    If `false`, shows files that should not be used in new content.
    """

    limit: int
    """Number of items to return. Default limit is 10, maximum limit is 100."""

    name: str
    """Search for files containing the given name."""

    parent_folder_ids: Annotated[Iterable[int], PropertyInfo(alias="parentFolderIds")]
    """Search files within given `folderId`."""

    path: str
    """Search files by path."""

    properties: SequenceNotStr[str]
    """A list of file properties to return."""

    size: int
    """Search files by exact file size in bytes."""

    size_gte: Annotated[int, PropertyInfo(alias="sizeGte")]
    """Search files by greater than or equal to file size.

    Can be used with `sizeLte` to create a range.
    """

    size_lte: Annotated[int, PropertyInfo(alias="sizeLte")]
    """Search files by less than or equal to file size.

    Can be used with `sizeGte` to create a range.
    """

    sort: SequenceNotStr[str]
    """Sort files by a given field."""

    type: str
    """Filter by provided file type."""

    updated_at: Annotated[Union[str, datetime], PropertyInfo(alias="updatedAt", format="iso8601")]
    """Search files by time of latest updated."""

    updated_at_gte: Annotated[Union[str, datetime], PropertyInfo(alias="updatedAtGte", format="iso8601")]
    """Search files by greater than or equal to time of latest update.

    Can be used with `updatedAtLte` to create a range.
    """

    updated_at_lte: Annotated[Union[str, datetime], PropertyInfo(alias="updatedAtLte", format="iso8601")]
    """Search files by less than or equal to time of latest update.

    Can be used with `updatedAtGte` to create a range.
    """

    url: str
    """Search by file URL."""

    width: int
    """Search files by width of image or video."""

    width_gte: Annotated[int, PropertyInfo(alias="widthGte")]
    """Search files by greater than or equal to width of image or video.

    Can be used with `widthLte` to create a range.
    """

    width_lte: Annotated[int, PropertyInfo(alias="widthLte")]
    """Search files by less than or equal to width of image or video.

    Can be used with `widthGte` to create a range.
    """
