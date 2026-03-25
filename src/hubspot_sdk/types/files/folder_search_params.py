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
    """
    The paging cursor token of the last successfully read resource will be returned
    as the `paging.next.after` JSON property of a paged response containing more
    results.
    """

    before: str

    created_at: Annotated[Union[str, datetime], PropertyInfo(alias="createdAt", format="iso8601")]

    created_at_gte: Annotated[Union[str, datetime], PropertyInfo(alias="createdAtGte", format="iso8601")]

    created_at_lte: Annotated[Union[str, datetime], PropertyInfo(alias="createdAtLte", format="iso8601")]

    id_gte: Annotated[int, PropertyInfo(alias="idGte")]

    id_lte: Annotated[int, PropertyInfo(alias="idLte")]

    ids: Iterable[int]

    limit: int
    """The maximum number of results to display per page."""

    name: str

    parent_folder_ids: Annotated[Iterable[int], PropertyInfo(alias="parentFolderIds")]

    path: str

    properties: SequenceNotStr[str]

    sort: SequenceNotStr[str]

    updated_at: Annotated[Union[str, datetime], PropertyInfo(alias="updatedAt", format="iso8601")]

    updated_at_gte: Annotated[Union[str, datetime], PropertyInfo(alias="updatedAtGte", format="iso8601")]

    updated_at_lte: Annotated[Union[str, datetime], PropertyInfo(alias="updatedAtLte", format="iso8601")]
