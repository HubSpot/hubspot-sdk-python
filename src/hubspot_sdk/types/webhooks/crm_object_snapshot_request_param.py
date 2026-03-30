# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo

__all__ = ["CrmObjectSnapshotRequestParam"]


class CrmObjectSnapshotRequestParam(TypedDict, total=False):
    object_id: Required[Annotated[int, PropertyInfo(alias="objectId")]]

    object_type_id: Required[Annotated[str, PropertyInfo(alias="objectTypeId")]]

    portal_id: Required[Annotated[int, PropertyInfo(alias="portalId")]]

    properties: Required[SequenceNotStr[str]]
