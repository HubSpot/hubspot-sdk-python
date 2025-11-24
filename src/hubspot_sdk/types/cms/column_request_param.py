# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo
from ..shared_params.option import Option

__all__ = ["ColumnRequestParam"]


class ColumnRequestParam(TypedDict, total=False):
    id: Required[int]
    """Column Id"""

    label: Required[str]
    """Label of the column"""

    name: Required[str]
    """Name of the column"""

    options: Required[Iterable[Option]]
    """Options to choose for select and multi-select columns"""

    type: Required[
        Literal[
            "BOOLEAN",
            "CODE",
            "COMPOSITE",
            "CTA",
            "CURRENCY",
            "DATE",
            "DATETIME",
            "EMBED",
            "FILE",
            "FOREIGN_ID",
            "HUBSPOT_VIDEO",
            "IMAGE",
            "JSON",
            "LOCATION",
            "MULTISELECT",
            "NULL",
            "NUMBER",
            "RICHTEXT",
            "SELECT",
            "TEXT",
            "URL",
            "VIDEO",
        ]
    ]
    """Type of the column"""

    foreign_column_id: Annotated[int, PropertyInfo(alias="foreignColumnId")]
    """The id of the column from another table to which the column refers/points to."""

    foreign_table_id: Annotated[int, PropertyInfo(alias="foreignTableId")]
    """The id of another table to which the column refers/points to."""

    max_number_of_characters: Annotated[int, PropertyInfo(alias="maxNumberOfCharacters")]

    max_number_of_options: Annotated[int, PropertyInfo(alias="maxNumberOfOptions")]
