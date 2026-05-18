# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Required, Annotated, TypedDict

from ....._utils import PropertyInfo

__all__ = ["FolderUpdateParams"]


class FolderUpdateParams(TypedDict, total=False):
    id: Required[str]
    """The unique ID of the content folder."""

    category: Required[int]
    """The type of object this folder applies to. Should always be LANDING_PAGE."""

    created: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]
    """The timestamp indicating when the content folder was created."""

    deleted_at: Required[Annotated[Union[str, datetime], PropertyInfo(alias="deletedAt", format="iso8601")]]
    """The timestamp (ISO8601 format) when this content folder was deleted."""

    name: Required[str]
    """The name of the folder which will show up in the app dashboard"""

    parent_folder_id: Required[Annotated[int, PropertyInfo(alias="parentFolderId")]]
    """The ID of the content folder this folder is nested under"""

    updated: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]
    """The timestamp indicating when the content folder was last updated."""

    archived: bool
    """Whether to return only results that have been archived."""
