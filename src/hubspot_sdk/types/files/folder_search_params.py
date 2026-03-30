# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from datetime import datetime
from typing_extensions import Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo

__all__ = ["FolderSearchParams"]


class FolderSearchParams(TypedDict, total=False):
    after: str
    """Offset search results by this value.

    The default offset is 0 and the maximum offset of items for a given search is
    10,000. Narrow your search down if you are reaching this limit.
    """

    before: str
    """Search folders updated before this timestamp.

    Time must be epoch time in milliseconds.
    """

    created_at: Annotated[Union[str, datetime], PropertyInfo(alias="createdAt", format="iso8601")]
    """Search folders by exact time of creation.

    Time must be epoch time in milliseconds.
    """

    created_at_gte: Annotated[Union[str, datetime], PropertyInfo(alias="createdAtGte", format="iso8601")]
    """Search folders by greater than or equal to time of creation.

    Can be used with createdAtLte to create a range.
    """

    created_at_lte: Annotated[Union[str, datetime], PropertyInfo(alias="createdAtLte", format="iso8601")]
    """Search folders by less than or equal to time of creation.

    Can be used with createdAtGte to create a range.
    """

    id_gte: Annotated[int, PropertyInfo(alias="idGte")]
    """Search folders by greater than or equal to ID.

    Can be used with idLte to create a range.
    """

    id_lte: Annotated[int, PropertyInfo(alias="idLte")]
    """Search folders by less than or equal to ID.

    Can be used with idGte to create a range.
    """

    ids: Iterable[int]
    """Search folders by multiple IDs. Comma-separated list of folder IDs."""

    limit: int
    """Number of items to return. Default limit is 10, maximum limit is 100."""

    name: str
    """Search for folders containing the specified name."""

    parent_folder_ids: Annotated[Iterable[int], PropertyInfo(alias="parentFolderIds")]

    path: str
    """Search folders by path."""

    properties: SequenceNotStr[str]
    """Properties that should be included in the returned folders."""

    sort: SequenceNotStr[str]
    """Sort results by given property.

    For example -name sorts by name field descending, name sorts by name field
    ascending.
    """

    updated_at: Annotated[Union[str, datetime], PropertyInfo(alias="updatedAt", format="iso8601")]
    """Search folders by exact time of latest updated.

    Time must be epoch time in milliseconds.
    """

    updated_at_gte: Annotated[Union[str, datetime], PropertyInfo(alias="updatedAtGte", format="iso8601")]
    """Search folders by greater than or equal to time of latest update.

    Can be used with updatedAtLte to create a range.
    """

    updated_at_lte: Annotated[Union[str, datetime], PropertyInfo(alias="updatedAtLte", format="iso8601")]
    """Search folders by less than or equal to time of latest update.

    Can be used with updatedAtGte to create a range.
    """
