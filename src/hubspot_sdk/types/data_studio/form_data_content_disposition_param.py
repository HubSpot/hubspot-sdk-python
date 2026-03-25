# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union
from datetime import datetime
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["FormDataContentDispositionParam"]


class FormDataContentDispositionParam(TypedDict, total=False):
    creation_date: Required[Annotated[Union[str, datetime], PropertyInfo(alias="creationDate", format="iso8601")]]
    """The date and time when the file was created, in ISO 8601 format."""

    file_name: Required[Annotated[str, PropertyInfo(alias="fileName")]]
    """
    A string indicating the name of the file associated with this content
    disposition.
    """

    modification_date: Required[
        Annotated[Union[str, datetime], PropertyInfo(alias="modificationDate", format="iso8601")]
    ]
    """The date and time when the file was last modified, in ISO 8601 format."""

    name: Required[str]
    """A string representing the name associated with this content disposition."""

    parameters: Required[Dict[str, str]]
    """
    An object containing additional parameters for the content disposition, with
    each parameter represented as a string.
    """

    read_date: Required[Annotated[Union[str, datetime], PropertyInfo(alias="readDate", format="iso8601")]]
    """The date and time when the file was last read, in ISO 8601 format."""

    size: Required[int]
    """An integer representing the size of the file in bytes."""

    type: Required[str]
    """A string representing the type of content disposition."""
