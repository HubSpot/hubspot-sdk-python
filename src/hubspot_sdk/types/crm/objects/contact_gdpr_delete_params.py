# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["ContactGdprDeleteParams"]


class ContactGdprDeleteParams(TypedDict, total=False):
    object_id: Required[Annotated[str, PropertyInfo(alias="objectId")]]
    """The ID of the company to delete."""

    id_property: Annotated[str, PropertyInfo(alias="idProperty")]
    """
    The name of a unique property, when identifying records by property instead of
    ID.
    """
