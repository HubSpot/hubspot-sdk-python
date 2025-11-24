# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["FileImportFromURLAsyncParams"]


class FileImportFromURLAsyncParams(TypedDict, total=False):
    access: Required[
        Literal[
            "HIDDEN_INDEXABLE",
            "HIDDEN_NOT_INDEXABLE",
            "HIDDEN_PRIVATE",
            "HIDDEN_SENSITIVE",
            "PRIVATE",
            "PUBLIC_INDEXABLE",
            "PUBLIC_NOT_INDEXABLE",
            "SENSITIVE",
        ]
    ]
    """PUBLIC_INDEXABLE: File is publicly accessible by anyone who has the URL.

    Search engines can index the file. PUBLIC_NOT_INDEXABLE: File is publicly
    accessible by anyone who has the URL. Search engines _can't_ index the file.
    PRIVATE: File is NOT publicly accessible. Requires a signed URL to see content.
    Search engines _can't_ index the file.
    """

    url: Required[str]
    """URL to download the new file from."""

    duplicate_validation_scope: Annotated[
        Literal["ENTIRE_PORTAL", "EXACT_FOLDER"], PropertyInfo(alias="duplicateValidationScope")
    ]
    """ENTIRE_PORTAL: Look for a duplicate file in the entire account.

    EXACT_FOLDER: Look for a duplicate file in the provided folder.
    """

    duplicate_validation_strategy: Annotated[
        Literal["NONE", "REJECT", "RETURN_EXISTING"], PropertyInfo(alias="duplicateValidationStrategy")
    ]
    """NONE: Do not run any duplicate validation.

    REJECT: Reject the upload if a duplicate is found. RETURN_EXISTING: If a
    duplicate file is found, do not upload a new file and return the found duplicate
    instead.
    """

    expires_at: Annotated[Union[str, datetime], PropertyInfo(alias="expiresAt", format="iso8601")]
    """Specifies the date and time when the file will expire."""

    folder_id: Annotated[str, PropertyInfo(alias="folderId")]
    """One of folderId or folderPath is required.

    Destination folderId for the uploaded file.
    """

    folder_path: Annotated[str, PropertyInfo(alias="folderPath")]
    """One of folderPath or folderId is required.

    Destination folder path for the uploaded file. If the folder path does not
    exist, there will be an attempt to create the folder path.
    """

    name: str
    """Name to give the resulting file in the file manager."""

    overwrite: bool
    """
    If true, will overwrite existing file if one with the same name and extension
    exists in the given folder. The overwritten file will be deleted and the
    uploaded file will take its place with a new ID. If unset or set as false, the
    new file's name will be updated to prevent colliding with existing file if one
    exists with the same path, name, and extension
    """

    ttl: str
    """Time to live.

    If specified the file will be deleted after the given time frame. If left unset,
    the file will exist indefinitely
    """
