# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["TableCloneDraftParams"]


class TableCloneDraftParams(TypedDict, total=False):
    copy_rows: Required[Annotated[bool, PropertyInfo(alias="copyRows")]]
    """Specifies whether to copy the rows during clone"""

    is_hubspot_defined: Required[Annotated[bool, PropertyInfo(alias="isHubspotDefined")]]
    """Indicates whether the table is defined by HubSpot."""

    new_label: Annotated[str, PropertyInfo(alias="newLabel")]
    """The new label for the cloned table"""

    new_name: Annotated[str, PropertyInfo(alias="newName")]
    """The new name for the cloned table"""
