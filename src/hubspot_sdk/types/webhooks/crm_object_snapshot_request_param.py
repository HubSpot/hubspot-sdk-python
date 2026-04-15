# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo

__all__ = ["CrmObjectSnapshotRequestParam"]


class CrmObjectSnapshotRequestParam(TypedDict, total=False):
    object_id: Required[Annotated[int, PropertyInfo(alias="objectId")]]
    """
    An integer representing the unique identifier of the CRM object for which the
    snapshot is being requested.
    """

    object_type_id: Required[Annotated[str, PropertyInfo(alias="objectTypeId")]]
    """A string representing the type identifier of the CRM object."""

    portal_id: Required[Annotated[int, PropertyInfo(alias="portalId")]]
    """An integer representing the unique identifier of the HubSpot portal."""

    properties: Required[SequenceNotStr[str]]
    """
    An array of strings, each representing a property of the CRM object to be
    included in the snapshot.
    """
