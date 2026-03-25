# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union
from datetime import datetime
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["ContentDispositionParam"]


class ContentDispositionParam(TypedDict, total=False):
    creation_date: Required[Annotated[Union[str, datetime], PropertyInfo(alias="creationDate", format="iso8601")]]
    """The date and time when the file was created, formatted as a date-time string."""

    file_name: Required[Annotated[str, PropertyInfo(alias="fileName")]]
    """
    The name of the file as a string, indicating the file's name in the content
    disposition.
    """

    modification_date: Required[
        Annotated[Union[str, datetime], PropertyInfo(alias="modificationDate", format="iso8601")]
    ]
    """
    The date and time when the file was last modified, formatted as a date-time
    string.
    """

    parameters: Required[Dict[str, str]]
    """
    An object containing additional parameters for the content disposition, with
    each parameter represented as a key-value pair of strings.
    """

    read_date: Required[Annotated[Union[str, datetime], PropertyInfo(alias="readDate", format="iso8601")]]
    """The date and time when the file was last read, formatted as a date-time string."""

    size: Required[int]
    """The size of the file as an integer, representing the file's size in bytes."""

    type: Required[str]
    """
    The type of content disposition, typically a string indicating how the content
    should be handled.
    """
